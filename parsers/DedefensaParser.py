from models.Article import Article
from parsers.BaseParser import BaseParser


class DedefensaParser(BaseParser):
    def parse_article_soup(self, soup):
        article = soup.find("div", {"class": "body article"})

        return {
            "content": article.getText(),
        }

    @staticmethod
    def format_article(parsed_article, metadata, author):
        return Article(
            date=metadata["date"],
            link=metadata["link"],
            title=metadata["title"],
            description="",
            content=parsed_article["content"],
            author=author
        )
