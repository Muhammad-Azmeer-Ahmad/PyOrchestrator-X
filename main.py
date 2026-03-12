import requests
from core.logger import orchestrator_logger as logger

def main():
    logger.info("🔍 Recon script started")

    # Example: fetch a single joke from a public API
    url = "https://official-joke-api.appspot.com/random_joke"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()

        # Log the joke as demonstration of online automation
        logger.info(f"Fetched joke: {data.get('setup')} - {data.get('punchline')}")

    except requests.RequestException as e:
        logger.error(f"Failed to fetch joke: {e}")

    logger.info("🔍 Recon script finished")


if __name__ == "__main__":
    main()
