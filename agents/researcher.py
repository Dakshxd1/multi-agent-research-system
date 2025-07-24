import os
import requests
from bs4 import BeautifulSoup

def search_web(query):
    url = "https://google.serper.dev/search"
    headers = {
        "X-API-KEY": os.getenv("SERPER_API_KEY"),
        "Content-Type": "application/json"
    }
    data = {"q": query, "num": 1}
    resp = requests.post(url, headers=headers, json=data)
    res = resp.json()
    organic = res.get('organic', [])
    return organic[0]['link'] if organic else None

def extract_article_text(url):
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, 'html.parser')
        paragraphs = soup.find_all('p')
        # Combine first few paragraphs for a summary
        content = " ".join(p.get_text() for p in paragraphs[:6])
        return content.strip()
    except Exception as e:
        print(f"❌ Error scraping {url}: {e}")
        return ""

def research_subtopics(subtopics):
    articles = []
    for sub in subtopics:
        print(f"🔍 Searching: {sub}")
        url = search_web(sub)
        if url:
            print(f"✅ Found URL: {url}")
            content = extract_article_text(url)
            articles.append({
                "subtopic": sub,
                "url": url,
                "content": content
            })
        else:
            print(f"⚠️ No URL found for: {sub}")
    return articles
