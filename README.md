# 🤖⚡PyOrchestrator X

**Automated Job Scraper & Dashboard** built with Python and Django.  
Scrapes jobs from LinkedIn, scores them based on relevance, tracks applications, and provides a clean dashboard UI for job management.

---

## 🔹 Features

- **LinkedIn Job Scraper:** Automatically fetches job postings.
- **Job Scoring Engine:** Scores jobs based on keywords and roles.
- **Job Analyzer:** Detects remote status and required experience.
- **Scheduler:** Automates scraping at defined intervals.
- **Dashboard:**  
  - Interactive job cards with applied tracking  
  - Tabs for categorizing jobs  
  - Calendar showing last 7 days of activity
- **Secure & Configurable:** Configurable keywords and roles in `config.py`.

---

## 🛠 Tech Stack

- **Backend:** Python 3.11, Django  
- **Frontend:** TailwindCSS, HTML, JS  
- **Scraping:** `requests`, `BeautifulSoup`  
- **Database:** SQLite (can be swapped with PostgreSQL)  
- **Logging & Scheduler:** Custom logging and job scheduling  

---

## ⚡ Installation

```bash
# Clone repo
git clone https://github.com/Muhammad-Azmeer-Ahmad/PyOrchestrator-X.git
cd PyOrchestrator-X

# Create virtual environment
python -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# Run scheduler
python manage.py scheduler

# Run Django server
python manage.py runserver
```
## 📁 File Structure:

```bash
PyOrchestratorX/
├── automations/       # Scraper, job scorer, analyzer, config
├── jobs/              # Django app for jobs, models & dashboard
├── dashboard/         # Views & URLs for dashboard
├── core/              # Logger, validators, executor
├── security/          # Command guard & secrets
├── storage/           # DB helpers
├── db.sqlite3         # Local database
├── manage.py          # Django management
├── main.py            # Optional entry point
└── requirements.txt   # Dependencies
```
