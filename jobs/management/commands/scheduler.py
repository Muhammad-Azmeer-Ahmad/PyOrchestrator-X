from django.core.management.base import BaseCommand
from core.logger import orchestrator_logger as logger

from jobs.scheduler import start_scheduler


class Command(BaseCommand):
    help = "Starts the PyOrchestratorX job scheduler"

    def handle(self, *args, **options):

        logger.info("Launching Scheduler Command...")

        try:
            start_scheduler()

        except KeyboardInterrupt:
            logger.warning("Scheduler stopped manually.")

        except Exception as e:
            logger.error(f"Scheduler crashed: {e}")
