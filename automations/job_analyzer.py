from automations.config import EXPERIENCE_TARGET
from jobs.models import JobListing


REMOTE_KEYWORDS = [
    "remote",
    "work from home",
    "anywhere",
    "distributed",
]


SENIOR_KEYWORDS = [
    "senior",
    "lead",
    "principal",
    "staff",
]


def analyze_job(job):

    text = f"{job.title} {job.description} {job.location}".lower()

    job.is_remote = detect_remote(text)

    job.experience_level = detect_experience(text)

    job.status = "ANALYZED"

    job.save()


def detect_remote(text):

    for word in REMOTE_KEYWORDS:
        if word in text:
            return True

    return False


def detect_experience(text):

    for word in EXPERIENCE_TARGET:
        if word in text:
            return "BEGINNER"

    for word in SENIOR_KEYWORDS:
        if word in text:
            return "SENIOR"

    return "MID"