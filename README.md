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
## 📚 Learning & Deep Dive

PyOrchestrator X was designed not just as a scraper, but as a **complete job automation and analytics platform**. Working on this project helped me learn and implement several advanced concepts in Python and Django:

### **1. Web Scraping & Data Extraction**
- Learned to fetch and parse live LinkedIn job postings using `requests` and `BeautifulSoup`.
- Handled real-world challenges like missing elements, rate-limiting, and dynamic URLs.
- Built a **robust scraper** that avoids crashes and logs errors cleanly.

### **2. Job Scoring & Relevance Analysis**
- Separated the **scoring engine** into its own module (`job_scorer.py`) for clean architecture.
- Used configurable **keywords** and **roles** to assign relevance scores automatically.
- Learned to make scoring logic flexible and scalable for future improvements.

### **3. Automation & Scheduling**
- Implemented a **scheduler** that can run scraping jobs automatically at defined intervals.
- Learned how to manage idle states, logging, and avoiding duplicate database entries.
- Integrated `update_or_create()` in Django to prevent duplicate jobs.

### **4. Django Backend & Dashboard**
- Designed a **dynamic dashboard** showing all jobs with tabs, status badges, and interactive checkboxes.
- Learned **template inheritance** (`base.html`) and reusable UI components.
- Built a **jobs calendar** visualizing last 7 days of scraped vs applied jobs.
- Handled **CSRF protection** for checkbox toggles and safe data updates.

### **5. Modular Architecture & Best Practices**
- Split functionality into logical modules: `scraper`, `job_scorer`, `job_analyzer`, `scheduler`.
- Learned the importance of separation of concerns for **readability and maintainability**.
- Implemented logging and validators to ensure robust code execution.

### **6. Deployment & Portfolio Readiness**
- Configured `.gitignore` and `requirements.txt` for **professional GitHub repository management**.
- Learned to push code **professionally** with commits, remote setup, and branch management.
- Prepared a demo-ready project with **UI, video, and documentation** for portfolio or Fiverr showcase.

---

**Outcome:**  
By the end of this project, I can confidently build **end-to-end Python automation platforms** that are scalable, maintainable, and visually appealing for dashboards.  
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

