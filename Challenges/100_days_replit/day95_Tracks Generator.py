import os
import requests
from requests.auth import HTTPBasicAuth
from openai import OpenAI

NEWS_API_KEY = os.getenv("NEWS_API_KEY")
ORGANISATION_ID = os.getenv("ORGANISATION_ID")
OPEN_API_KEY = os.getenv("OPEN_API_KEY")
SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")

SPOTIFY_URL = "https://accounts.spotify.com/api/token"
NEWS_URL = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={NEWS_API_KEY}"

# Authenticate with OpenAI
OPEN_AI_CLIENT = OpenAI(api_key=OPEN_API_KEY, organization=ORGANISATION_ID)

# Authenticate with Spotify
auth = HTTPBasicAuth(SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET)
data = {"grant_type": "client_credentials"}
response = requests.post(url=SPOTIFY_URL, data=data, auth=auth)
SPOTIFY_ACCESS_TOKEN = response.json()["access_token"]


def get_news():
    """Function to fetch news articles"""
    results = requests.get(NEWS_URL)
    data = results.json()

    articles = []
    for article in data["articles"][:5]:  # Take 5 news articles
        if article["title"] != "[Removed]":
            articles.append({"title": article["title"], "content": article["content"]})

    return articles


def summarize_articles(articles):
    """Function to summarize articles using OpenAI"""
    raw_article = "\n".join(
        [
            f"Title: {article['title']}\nShort Content: {article['content']}\n-----------\n"
            for article in articles
        ]
    )

    response = OPEN_AI_CLIENT.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": f"Give me a summary based on these articles:\n{raw_article}",
            },
        ],
    )

    return response.choices[0].message.content


def search_spotify(query):
    """Function to search for tracks on Spotify"""
    url = "https://api.spotify.com/v1/search"
    full_url = f"{url}?q={query}&type=track&limit=5"

    headers = {"Authorization": f"Bearer {SPOTIFY_ACCESS_TOKEN}"}
    response = requests.get(full_url, headers=headers)
    tracks = response.json()["tracks"]["items"]

    return tracks


def main():
    """Main function"""
    # Get news articles
    articles = get_news()

    # Summarize articles
    summary = summarize_articles(articles)

    # Search Spotify based on the OpenAI summary
    tracks = search_spotify(summary)

    # Print Spotify tracks
    print(tracks)


if __name__ == "__main__":
    main()
