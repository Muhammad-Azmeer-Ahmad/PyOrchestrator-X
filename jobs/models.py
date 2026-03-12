from django.db import models

# ----------------------------
# Scheduler Job Model
# ----------------------------
class Job(models.Model):
    name = models.CharField(max_length=200)
    entry_point = models.CharField(max_length=255)
    interval_minutes = models.IntegerField(default=60)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


# ----------------------------
# Job Execution Logs
# ----------------------------
class JobRun(models.Model):
    STATUS_CHOICES = [
        ("RUNNING", "Running"),
        ("SUCCESS", "Success"),
        ("FAILED", "Failed"),
    ]

    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    started_at = models.DateTimeField()
    finished_at = models.DateTimeField(null=True, blank=True)
    exit_code = models.IntegerField(null=True, blank=True)
    stderr = models.TextField(blank=True)

    def __str__(self):
        return f"{self.job.name} - {self.status}"


# ----------------------------
# Scraped Job Listings
# ----------------------------
class JobListing(models.Model):
    # Choice Constants
    STATUS_CHOICES = [
        ("NEW", "New"),
        ("ANALYZED", "Analyzed"),
        ("CV_GENERATED", "CV Generated"),
        ("APPLIED", "Applied"),
        ("FAILED", "Failed"),
    ]

    EXPERIENCE_CHOICES = [
        ("BEGINNER", "Beginner"),
        ("MID", "Mid Level"),
        ("SENIOR", "Senior"),
    ]

    # Core Fields
    title = models.CharField(max_length=255)
    company = models.CharField(max_length=255, null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(blank=True)
    url = models.URLField(unique=True)

    # --- New Fields Added ---
    # default="UNKNOWN" handles existing rows during migration
    source = models.CharField(max_length=100, default="UNKNOWN")
    experience_level = models.CharField(
        max_length=20,
        choices=EXPERIENCE_CHOICES,
        default="MID"
    )
    # ------------------------

    # Job Details
    is_remote = models.BooleanField(default=False)
    is_part_time = models.BooleanField(default=False)
    salary_range = models.CharField(max_length=100, null=True, blank=True)

    # AI & Processing
    relevance_score = models.IntegerField(default=0)
    ai_summary = models.TextField(null=True, blank=True)
    customized_cv_path = models.FileField(
        upload_to="custom_cvs/", null=True, blank=True
    )

    # Status & Tracking
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="NEW")
    scraped_at = models.DateTimeField(auto_now_add=True)
    applied_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.title} @ {self.company} ({self.source})"