from bs4 import BeautifulSoup
import dateutil.parser

from crawlers import crawl_link
from models.Article import Article


class BaseParser:
    def __init__(self):
        self.articles = []

    def extract_rss_item_data(self, info):
        shown_date = self.extract_date(info)
        usable_date = dateutil.parser.parse(shown_date)

        link = info.find("link").getText()
        url_without_fragment = link.split("#")[0]

        return {
            "link": url_without_fragment,
            "date": usable_date,
            "title": info.find("title").getText(),
            "description": info.find("description").getText(),
        }

    @staticmethod
    def extract_date(info):
        pubDate = info.find("pubDate")
        if pubDate:
            return pubDate.getText()

        dcDate = info.find("dc:date")
        if dcDate:
            return dcDate.getText()

        return None

    @staticmethod
    def get_article_soup(link):
        return BeautifulSoup(crawl_link(link), 'lxml')

    def parse_article_soup(self, soup):
        return {"content": ""}

    @staticmethod
    def format_article(parsed_article, metadata, author):
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
            try:
                article_data = self.extract_rss_item_data(raw_article)
                article_soup = self.get_article_soup(article_data["link"])
                parsed_article = self.parse_article_soup(article_soup)

                if parsed_article["content"]:
                    result = self.format_article(parsed_article, article_data, author=author)
                    self.articles.append(result)

            except Exception as error:
                print(f"parse article error: {str(error)}")
