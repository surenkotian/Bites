from fastapi import FastAPI
from app.news_fetcher import get_latest_news

app = FastAPI(title="Bites API")

@app.get("/")
def home():
    return {"message": "Welcome to Bites API!"}

@app.get("/news")
def fetch_news():
    news = get_latest_news()
    return {"articles": news}
