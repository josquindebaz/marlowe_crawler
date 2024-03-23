from datetime import datetime

from models.Article import Article
from parsers.BaseParser import BaseParser


class BfmTvParser(BaseParser):
    def parse_article_soup(self, soup):
        paragraphs = [
            paragraph.getText() for paragraph in soup.findAll("p")
        ]

        chapo = soup.find("div", {"class": "chapo"})
        description = chapo.getText() if chapo else ""

        return {
            "content": "\n".join(paragraphs[:-3]),
            "description": description
        }

    @staticmethod
    def format_article(parsed_article, metadata, author):
        return Article(
            date=metadata["date"],
            link=metadata["link"],
            title=metadata["title"],
            description=parsed_article["description"],
            content=parsed_article["content"],
            author=author
        )
