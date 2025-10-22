from newsapi import NewsApiClient
from app.summarizer import summarize_text
import os

# Use environment variable so the key is not committed to git
api_key = os.getenv("NEWSAPI_KEY")
if not api_key:
    raise EnvironmentError("Missing NEWSAPI_KEY environment variable. Set it locally or in GitHub Secrets.")

newsapi = NewsApiClient(api_key=api_key)

def get_latest_news(limit: int = 5):
    top_headlines = newsapi.get_top_headlines(language='en', country='us')
    articles = top_headlines.get('articles', []) if isinstance(top_headlines, dict) else []

    summarized = []
    for a in articles[:limit]:
        # be defensive about missing fields
        description = a.get('description') or a.get('content') or ''
        summary = summarize_text(description) if description else ''
        summarized.append({
            "title": a.get('title'),
            "summary": summary,
            "url": a.get('url'),
            "source": (a.get('source') or {}).get('name')
        })
    return summarized