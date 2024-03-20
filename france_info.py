from bs4 import BeautifulSoup
from datetime import datetime

import database

from crawlers import crawl_link
from models.Article import Article
from rss_parser import get_rss_soup


class Parser:
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
        result = soup.find("div", {"class": "c-body"})
        if not result:
            return {"content": ""}

        return {
            "content": result.getText()
        }

    def format_article(self, parsed_article, metadata, author):
        return Article(
            date=metadata["date"],
            link=metadata["link"],
            title=metadata["title"],
            description=metadata["description"],
            content=parsed_article["content"],
            author=author
        )

    def process_articles(self, rss):
        for raw_article in rss["articles"]:
            article_data = self.extract_rss_item_data(raw_article)
            article_soup = self.get_article_soup(article_data["link"])
            parsed_article = self.parse_article_soup(article_soup)

            result = self.format_article(parsed_article, article_data, author="franceinfo")
            self.articles.append(result)


if __name__ == "__main__":
    rss_links = [
        'https://www.francetvinfo.fr/politique.rss',
        'https://www.francetvinfo.fr/societe.rss',
        'https://www.francetvinfo.fr/faits-divers.rss',
        'https://www.francetvinfo.fr/sante.rss',
        'https://www.francetvinfo.fr/economie/tendances.rss',
        'https://www.francetvinfo.fr/monde.rss'
    ]

    for rss_link in rss_links:
        rss_content = get_rss_soup(crawl_link(rss_link))
        parser = Parser()
        parser.process_articles(rss_content)

        print(rss_content["description"], " -> crawled ", len(parser.articles), " on ", len(rss_content["articles"]))

        for article in parser.articles:
            # print(f"Inserting {article.title}")
            database.insert_in_table(article)
