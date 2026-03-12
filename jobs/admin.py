from django.contrib import admin
from .models import Job, JobRun, JobListing


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ("name", "entry_point", "interval_minutes", "is_active", "created_at")
    list_filter = ("is_active",)
    search_fields = ("name", "entry_point")


@admin.register(JobRun)
class JobRunAdmin(admin.ModelAdmin):
    list_display = ("job", "status", "started_at", "finished_at")
    list_filter = ("status",)
    search_fields = ("job__name",)


@admin.register(JobListing)
class JobListingAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "company",
        "location",
        "is_remote",
        "relevance_score",
        "status",
        "scraped_at",
    )

    list_filter = (
        "is_remote",
        "is_part_time",
        "status",
    )

    search_fields = (
        "title",
        "company",
        "description",
    )

    ordering = ("-scraped_at",)