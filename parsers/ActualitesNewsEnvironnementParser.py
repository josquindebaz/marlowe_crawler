from models.Article import Article
from parsers.BaseParser import BaseParser

import re


class ActualitesNewsEnvironnementParser(BaseParser):
    def parse_article_soup(self, soup):
        article = soup.find("span", {"class": "Actu_Article_Bloc"})
        description = article.find("span", {"class": "Actu_Article_Chapeau"}).getText()
        paragraphs = [
            re.sub("\xa0", "", paragraph.getText(strip=True))
            for paragraph in article.findAll("p")[:-2]
            if paragraph['style'] == 'TEXT-ALIGN:'
        ]

        return {
            "content": "\n".join(paragraphs),
            "description": description,
            "title": soup.find("title").getText()
        }

    @staticmethod
    def format_article(parsed_article, metadata, author):
        return Article(
            date=metadata["date"],
            link=metadata["link"],
            title=parsed_article["title"],
            description=parsed_article["description"],
            content=parsed_article["content"],
            author=author
        )
