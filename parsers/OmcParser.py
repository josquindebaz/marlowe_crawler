from models.Article import Article
from parsers.BaseParser import BaseParser


class OmcParser(BaseParser):
    def parse_article_soup(self, soup):
        article = soup.find("div", {"id": "mainContent"})
        article.find("div", {"class", "base-share"}).decompose()

        return {
            "content": article.getText()
        }

    @staticmethod
    def format_article(parsed_article, metadata, author):
        return Article(
            date=metadata["date"],
            link=metadata["link"],
            title=metadata["title"],
            description=metadata["description"],
            content=metadata["description"] + parsed_article["content"],
            author=author
        )
