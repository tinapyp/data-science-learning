import os
import requests
from openai import OpenAI

NEWS_API_KEY = os.getenv("NEWS_API_KEY")
ORGANISATION_ID = os.getenv("ORGANISATION_ID")
OPEN_API_KEY = os.getenv("OPEN_API_KEY")
client = OpenAI(api_key=OPEN_API_KEY, organization=ORGANISATION_ID)

url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={NEWS_API_KEY}"

results = requests.get(url)
data = results.json()

raw_article = ""
for article in data["articles"]:
    if article["title"] == "[Removed]":
        continue
    else:
        raw_article += f"Title: {article['title']}"
        raw_article += f"Short Content : {article['content']}\n ----------- \n"


response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "user",
            "content": f"""Summarize of today news headline for me!, in essay format
            {raw_article}
            """,
        },
    ],
)

print(response.choices[0].message.content)
