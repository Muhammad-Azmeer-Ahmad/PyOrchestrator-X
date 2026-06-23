# PyOrchestrator-X

Automated job discovery platform built with Python and Django. Scrapes LinkedIn job listings, scores them by relevance against configurable keywords and roles, and tracks application status in a dashboard with activity visualization.

---

## Features

- **LinkedIn Scraper** — Fetches live job postings using `requests` and `BeautifulSoup`
- **Scoring Engine** — Assigns relevance scores based on configurable keywords and target roles
- **Job Analyzer** — Detects remote status and required experience level
- **Scheduler** — Automates scraping at defined intervals; uses `update_or_create()` to prevent duplicates
- **Dashboard** — Interactive job cards, status tabs, CSRF-protected application toggles, and a 7-day activity calendar
- **Configurable** — Set target keywords and roles in `automations/config.py`

---

## Tech Stack

| Layer     | Technology                         |
|-----------|------------------------------------|
| Backend   | Python 3.11, Django                |
| Frontend  | HTML, TailwindCSS, JavaScript      |
| Scraping  | requests, BeautifulSoup4           |
| Database  | SQLite (swappable with PostgreSQL) |

---

## Getting Started

```bash
git clone https://github.com/Muhammad-Azmeer-Ahmad/PyOrchestrator-X.git
cd PyOrchestrator-X

python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

pip install -r requirements.txt

python manage.py migrate
python manage.py scheduler      # Start the scraping scheduler
python manage.py runserver      # Start the Django server
```

Open `http://127.0.0.1:8000` in your browser.

---

## Configuration

Edit `automations/config.py` to set your target job keywords and roles before running the scheduler.

---

## Project Structure

```
PyOrchestratorX/
├── automations/       # Scraper, scorer, analyzer, scheduler, config
├── jobs/              # Django app — models, views, dashboard
├── dashboard/         # URLs and views for the dashboard
├── core/              # Logger, validators, executor
├── security/          # Command guard and secrets handling
├── storage/           # Database helpers
├── manage.py
├── main.py
└── requirements.txt
```

---

## License

MIT
