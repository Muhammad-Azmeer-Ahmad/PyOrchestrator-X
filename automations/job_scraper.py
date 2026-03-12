

import requests
from bs4 import BeautifulSoup
from jobs.models import JobListing
import logging
from automations.job_analyzer import analyze_job
from automations.config import KEYWORDS, ROLES
import time

logger = logging.getLogger(__name__)

HEADERS = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
    "Referer": "https://www.google.com/",
}


# -----------------------------
# Scoring Engine
# -----------------------------
def score_job(text: str) -> int:
    score = 0
    for kw in KEYWORDS:
        if kw.lower() in text.lower():
            score += 2
    for role in ROLES:
        if role.lower() in text.lower():
            score += 3
    return score


# -----------------------------
# LinkedIn Scraper
# -----------------------------
def scrape_linkedin():
    jobs = []

    url = "https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?keywords=Python"

    try:
        logger.info("Scraping LinkedIn Jobs...")
        response = requests.get(url, headers=HEADERS, timeout=15)
        if response.status_code != 200:
            logger.error(f"LinkedIn returned status {response.status_code}")
            return jobs

        soup = BeautifulSoup(response.text, "html.parser")
        cards = soup.find_all("li")

        for card in cards:
            title_tag = card.find("h3", class_="base-search-card__title")
            company_tag = card.find("h4", class_="base-search-card__subtitle")
            link_tag = card.find("a", class_="base-card__full-link")

            if not title_tag or not link_tag:
                continue

            title = title_tag.text.strip()
            company = company_tag.text.strip() if company_tag else "Unknown"
            url = link_tag["href"].split("?")[0].strip()

            jobs.append({
                "title": title,
                "company": company,
                "url": url,
                "description": "View on LinkedIn",
                "platform": "LinkedIn"
            })

            # Optional: avoid rate limiting
            time.sleep(0.2)

    except Exception as e:
        logger.error(f"LinkedIn Error: {e}")

    return jobs


# -----------------------------
# Main Entry Point
# -----------------------------
def run():
    logger.info("Starting PyOrchestratorX Job Fetch (LinkedIn Only)...")

    all_scraped = scrape_linkedin()
    scraped_count = len(all_scraped)
    logger.info(f"Total jobs scraped: {scraped_count}")

    saved_count = 0
    valid_fields = [f.name for f in JobListing._meta.get_fields()]

    for data in all_scraped:
        job_defaults = {
            "title": data["title"],
            "company": data["company"],
            "description": data["description"],
            "relevance_score": score_job(data["title"]),
            "status": "NEW"
        }
        if "source" in valid_fields:
            job_defaults["source"] = data["platform"]

        # Use update_or_create to avoid duplicates & update existing jobs
        obj, created = JobListing.objects.update_or_create(
            url=data["url"],
            defaults=job_defaults
        )

        # Always analyze job (remote, experience)
        analyze_job(obj)

        if created:
            saved_count += 1

    logger.info(f"Run complete. Scraped: {scraped_count} | New Saved: {saved_count}")
    return {"scraped": scraped_count, "saved": saved_count}


if __name__ == "__main__":
    print(run())