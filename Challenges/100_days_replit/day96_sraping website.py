import requests
from bs4 import BeautifulSoup

url = "https://news.ycombinator.com/"

response = requests.get(url).text

soup = BeautifulSoup(response, "html.parser")

news_all = soup.find_all("a")

for news in news_all:
    if "SQL" in news.text:
        print(news.text)
        print(f"https://news.ycombinator.com/{news['href']}", "\n")
