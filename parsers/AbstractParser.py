from bs4 import BeautifulSoup
from datetime import datetime

from crawlers import crawl_link
from models.Article import Article


class AbstractParser:
    def __init__(self):
        self.articles = []

    def extract_rss_item_data(self, info):
        return {
            "link": info.find("link").getText(),
            "date": datetime.strptime(info.find("pubDate").getText(), "%a, %d %b %Y %H:%M:%S %z"),
            "title": info.find("title").getText(),
            "description": info.find("description").getText(),
        }

    def get_article_soup(self, link):
        return BeautifulSoup(crawl_link(link), 'lxml')

    def parse_article_soup(self, soup):
        return {"content": ""}

    def format_article(self, parsed_article, metadata, author):
        return Article(
            date=metadata["date"],
            link=metadata["link"],
            title=metadata["title"],
            description=metadata["description"],
            content=parsed_article["content"],
            author=author
        )

    def process_articles(self, rss, author):
        for raw_article in rss["articles"]:
            article_data = self.extract_rss_item_data(raw_article)
            article_soup = self.get_article_soup(article_data["link"])
            parsed_article = self.parse_article_soup(article_soup)

            result = self.format_article(parsed_article, article_data, author=author)
            self.articles.append(result)
