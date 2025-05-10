from parsers.BaseParser import BaseParser


class LeMondeParser(BaseParser):
    def parse_article_soup(self, soup):
        paywall = soup.find("p", {"class": "article__status"})
        if paywall:
            return {"content": ""}

        chapo = soup.find("meta", {"name": "description"})["content"]

        paragraphs = [
            paragraph.getText() for paragraph in soup.findAll("p", {"class": "article__paragraph"})
        ]

        return {
            "content": "\n".join(paragraphs),
            "description": chapo
        }
