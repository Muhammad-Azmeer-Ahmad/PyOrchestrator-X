import traceback
from django.utils import timezone

from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.interval import IntervalTrigger

from jobs.models import Job, JobRun
from core.executor import Executor
from core.validators import TaskValidator
from core.logger import orchestrator_logger as logger


# ✅ Use BlockingScheduler for Django management command
scheduler = BlockingScheduler()

# Single executor instance
executor = Executor(TaskValidator())


def run_job(job: Job):
    """
    Executes a job and stores results into JobRun.
    """

    logger.info(f"Running job: {job.name}")

    job_run = JobRun.objects.create(
        job=job,
        status="RUNNING",
        started_at=timezone.now()
    )

    try:
        # Execute task
        executor.run(job.entry_point)

        # Mark success
        job_run.status = "SUCCESS"
        job_run.exit_code = 0

    except Exception:
        logger.error(f"Job failed: {job.name}")
        job_run.status = "FAILED"
        job_run.exit_code = 1
        job_run.stderr = traceback.format_exc()

    finally:
        job_run.finished_at = timezone.now()
        job_run.save()

        logger.info(f"JobRun saved: {job.name} → {job_run.status}")


def start_scheduler():
    """
    Loads all active jobs from DB and schedules them.
    """

    logger.info("Loading jobs from database...")

    # ✅ Remove all previous jobs before re-adding
    scheduler.remove_all_jobs()

    active_jobs = Job.objects.filter(is_active=True)

    if not active_jobs.exists():
        logger.warning("No active jobs found. Scheduler will run idle.")
        return

    for job in active_jobs:

        # ✅ Prevent invalid interval values
        if job.interval_minutes < 1:
            logger.warning(
                f"Skipping job '{job.name}' because interval_minutes < 1"
            )
            continue

        trigger = IntervalTrigger(minutes=job.interval_minutes)

        scheduler.add_job(
            run_job,
            trigger=trigger,
            args=[job],
            id=str(job.id),
            name=job.name,
            replace_existing=True
        )

        logger.info(
            f"Scheduled: {job.name} every {job.interval_minutes} min"
        )

    logger.info("Scheduler started successfully.")

    # ✅ BLOCK FOREVER so jobs actually execute
    scheduler.start()
