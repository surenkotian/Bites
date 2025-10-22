# 📰 Bites – AI-Powered Quick News Summarizer

**Tagline:** *“Stay informed in seconds — AI-summarized, verified, and real-time.”*

---

## Overview

**Bites** is a lightweight, AI-driven news aggregator that delivers concise, verified, and real-time news summaries. It pulls data from trusted sources and verified Twitter/X accounts, summarizes long articles into 2–3 sentence “bites,” and displays them in a clean, modern, fast-loading web interface. Users can receive instant notifications for breaking news and browse top headlines by category.

---

## Features

- **AI Summarization:** Compress long articles into short, readable summaries using OpenAI GPT or HuggingFace models.  
- **Multi-source Aggregation:** Fetches news from NewsAPI, RSS feeds, and verified X (Twitter) accounts.  
- **Category Filters:** Browse news by categories like Tech, World, Sports, Business, Entertainment, etc.  
- **Real-Time Notifications:** Push notifications for breaking news on desktop or mobile.  
- **Lightweight & Fast:** Minimalistic UI, responsive, and low latency.  
- **Scalable:** Ready for adding personalization, text-to-speech summaries, or mobile app integration.  

---

## Project Structure

```

bites/
│
├── backend/
│   ├── venv/               # Virtual environment
│   ├── app/
│   │   ├── main.py          # FastAPI entrypoint
│   │   ├── news_fetcher.py  # Fetch news from APIs
│   │   ├── summarizer.py    # AI summarization logic
│   │   ├── twitter_feed.py  # Fetch tweets from verified accounts
│   │   ├── db.py            # SQLite DB setup
│   │   ├── models.py        # DB models
│   │   └── routes/
│   │       ├── news_routes.py
│   │       └── twitter_routes.py
│   └── requirements.txt
│
└── frontend/
├── src/
│   ├── components/      # React UI components
│   ├── pages/           # Pages like Home, Categories
│   └── App.jsx
├── package.json

````

---

## Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/bites.git
cd bites/backend
````

### 2. Setup Backend

```bash
python -m venv venv
# Activate venv
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

pip install -r requirements.txt
```

### 3. Setup `.env` File

Create a `.env` file in `backend/`:

```
NEWS_API_KEY=your_newsapi_key
OPENAI_API_KEY=your_openai_key
```

### 4. Run Backend

```bash
uvicorn app.main:app --reload
```

Visit `http://127.0.0.1:8000/news` to test API.

---

### 5. Setup Frontend

```bash
cd ../frontend
npm install
npm start
```

* Access the app at `http://localhost:3000`
* The frontend calls the backend API for live news and summaries.

---

## Usage

* Browse news by category (Tech, World, Sports, etc.)
* Click on a news card to see AI-generated summary.
* Enable push notifications to get breaking news alerts.
* Summaries are generated automatically by AI, saving reading time.

---

## Tech Stack

| Layer         | Technology                                             |
| ------------- | ------------------------------------------------------ |
| Frontend      | React, TailwindCSS, Framer Motion                      |
| Backend       | Python, FastAPI, Uvicorn                               |
| AI Layer      | OpenAI GPT-4-turbo / HuggingFace Summarizer            |
| News Sources  | NewsAPI, RSS feeds, X/Twitter via `snscrape` or Tweepy |
| Database      | SQLite (lightweight)                                   |
| Notifications | OneSignal / Push.js / Firebase Cloud Messaging         |
| Hosting       | Vercel (frontend), Render (backend)                    |

---

## Future Improvements

* User login & personalized news feed
* Text-to-speech summaries for accessibility
* Mobile PWA version
* Trending news map and analytics
* Email or Telegram daily digest

---

## Contributing

1. Fork the repository
2. Create a branch: `git checkout -b feature-name`
3. Commit your changes: `git commit -m "Description"`
4. Push: `git push origin feature-name`
5. Create a Pull Request

---

## License

MIT License © 2025 Suren Kotian

---

## Contact

* **Project Author:** Suren Kotian
* **Email:** [surenkotian10@gmail.com](mailto:surenkotian10@gmail.com)
* **GitHub:** [https://github.com/surenkotian](https://github.com/surenkotian)

```


