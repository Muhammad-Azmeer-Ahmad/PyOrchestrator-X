from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.utils.timezone import now
from datetime import datetime, timedelta

from .models import Job, JobRun, JobListing


def dashboard(request):

    # Scheduler Jobs
    jobs = Job.objects.all().order_by("-created_at")
    runs = JobRun.objects.all().order_by("-started_at")[:10]

    # Scraped Job Listings
    all_jobs = JobListing.objects.all().order_by("-scraped_at")
    remote_jobs = JobListing.objects.filter(is_remote=True)
    beginner_jobs = JobListing.objects.filter(experience_level="BEGINNER")
    applied_jobs = JobListing.objects.filter(applied_at__isnull=False)

    tabs = [
        ("all", all_jobs),
        ("remote", remote_jobs),
        ("beginner", beginner_jobs),
        ("applied", applied_jobs),
    ]

    # Calendar data (last 7 days)
    calendar = []
    today = datetime.today().date()

    for i in range(6, -1, -1):
        day = today - timedelta(days=i)

        scraped_count = JobListing.objects.filter(scraped_at__date=day).count()
        applied_count = JobListing.objects.filter(applied_at__date=day).count()

        calendar.append({
            "date": day.strftime("%d %b"),
            "scraped_count": scraped_count,
            "applied_count": applied_count,
        })

    context = {
        "tabs": tabs,
        "runs": runs,
        "total_jobs": all_jobs.count(),
        "active_jobs": jobs.filter(is_active=True).count(),
        "failed_runs": JobRun.objects.filter(status="FAILED").count(),
        "success_runs": JobRun.objects.filter(status="SUCCESS").count(),
        "calendar": calendar,
    }

    return render(request, "jobs/dashboard.html", context)


def toggle_apply(request, job_id):

    if request.method == "POST":

        job = get_object_or_404(JobListing, id=job_id)

        if job.applied_at:
            job.applied_at = None
        else:
            job.applied_at = now()

        job.save()

        return JsonResponse({
            "status": "ok",
            "applied": bool(job.applied_at)
        })

    return JsonResponse({"status": "error"})