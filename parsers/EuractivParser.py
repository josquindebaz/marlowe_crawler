from parsers.BaseParser import BaseParser


class EuractivParser(BaseParser):
    def parse_article_soup(self, soup):
        chapo = soup.find("p", {"class": "c-news-detail__sub-title"}).getText()

        paragraphs = [
            paragraph.getText() for paragraph in soup.findAll("p")
            if paragraph.attrs == {"style" : "text-align: left"}
        ]

        return {
            "content":  chapo + "\n" + "\n".join(paragraphs),
        }
