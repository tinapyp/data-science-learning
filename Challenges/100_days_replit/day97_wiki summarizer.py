import os
import requests
from bs4 import BeautifulSoup
from openai import OpenAI

ORGANISATION_ID = os.getenv("ORGANISATION_ID")
OPEN_API_KEY = os.getenv("OPEN_API_KEY")
client = OpenAI(api_key=OPEN_API_KEY, organization=ORGANISATION_ID)


def get_summarize(raw_article_text):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": f"""Summarize today's news headline for me!, in essay format
                              {raw_article_text}
                              """,
            },
        ],
    )

    summarize_article = response.choices[0].message.content

    return summarize_article


def get_article(url):
    response = requests.get(url).text
    soup = BeautifulSoup(response, "html.parser")
    articles = soup.find("div", class_="mw-content-ltr mw-parser-output").find_all("p")

    article_text = ""
    for paragraph in articles:
        article_text += paragraph.text

    return article_text


def get_citations(url):
    response = requests.get(url).text
    soup = BeautifulSoup(response, "html.parser")
    citations = soup.find(
        "div", class_="mw-references-wrap mw-references-columns"
    ).find_all("p")

    citation_text = ""
    for data in citations:
        citation_text += data.text

    return citation_text


def main():
    url = input("Paste Wiki URL> ")
    article_text = get_article(url)
    citation_text = get_citations(url)
    summarized_article = get_summarize(article_text)

    print(summarized_article, "\n", citation_text)


if __name__ == "__main__":
    main()
