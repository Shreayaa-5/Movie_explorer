# 🎬 Tamil Movie Explorer

A full-stack project that scrapes the **Top 100 Tamil Movies from IMDb** using **Selenium** and displays them in a modern, interactive web interface built with **Flask**.

---

# 🚀 Project Overview
This project solves the **"Sticky Page" problem** on modern websites by using browser automation to **scroll and click like a human**.  
It collects movie data from IMDb and serves it through a **Python Flask API** to a clean **dark-themed web interface**.

---

# ✨ Features
- **Intelligent Scraper**  
  Uses **Selenium** to bypass IMDb's 25-movie limit and capture **100+ unique Tamil movies**.

- **Data Deduplication**  
  Python logic ensures the same movie is **never saved twice**.

- **CSV Database**  
  Scraped movie data is stored in a structured  
  `tamil_movies_detailed.csv`.

- **Flask Web App**  
  A lightweight backend that serves movie data to the browser.

- **Modern UI**  
  Interactive **Movie Card interface** with **Next / Previous navigation**.

---

# 🛠️ Tech Stack

| Component | Technology |
|-----------|------------|
| Language | Python 3.12+ |
| Web Scraping | Selenium, BeautifulSoup4, Webdriver-Manager |
| Backend | Flask |
| Frontend | HTML5, CSS3, Vanilla JavaScript |
| Data Storage | CSV |

---

# 📦 Installation & Setup

## 1️⃣ Clone the Project
```bash
git clone https://github.com/YOUR_USERNAME/IMDB-Tamil-Explorer.git
cd IMDB-Tamil-Explorer
```

---

## 2️⃣ Create & Activate Virtual Environment

```bash
python -m venv .venv
```

### Windows
```bash
.\.venv\Scripts\activate
```

### Mac / Linux
```bash
source .venv/bin/activate
```

---

## 3️⃣ Install Required Libraries

```bash
pip install selenium webdriver-manager beautifulsoup4 flask requests
```

---

# 🎮 How to Run

## Step 1: Scrape the Data

Run the scraper to generate the movie dataset.

```bash
python scraper.py
```

A Chrome browser will open and automatically scroll to collect movie data.

---

## Step 2: Start the Flask Web App

```bash
python app.py
```

---

## Step 3: Open in Browser

Visit:

```
http://127.0.0.1:5000
```

You will see the **interactive Tamil Movie Explorer interface**.

---

# 📂 Project Structure

```
IMDB/
│
├── app.py                     # Flask server & API
├── scraper.py                 # Selenium scraping script
├── tamil_movies_detailed.csv  # Generated movie dataset
├── requirements.txt           # Python dependencies
├── .gitignore                 # Prevents uploading .venv
│
└── templates/
    └── index.html             # Frontend UI
```

---

# 🎓 Teacher's Final Checklist

Before pushing the project to GitHub:

✔ Ensure `.gitignore` is present (to ignore `.venv`)  
✔ Update dependencies:

```bash
pip freeze > requirements.txt
```

✔ Make sure `tamil_movies_detailed.csv` exists so the Flask app does not crash on first run.

---

# 📚 Learning Outcomes

This project demonstrates:

- Web scraping using **Selenium**
- Handling **dynamic webpages**
- Building a **Flask backend**
- Creating a **simple interactive frontend**
- Structuring a **real-world full-stack project**

---

# 👨‍💻 Author
Developed as a **learning project for Web Scraping and Full-Stack Development**.
