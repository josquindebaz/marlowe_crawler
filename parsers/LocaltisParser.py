from parsers.BaseParser import BaseParser


class LocaltisParser(BaseParser):
    def parse_article_soup(self, soup):
        chapo = soup.find("div", {"class": "lead"}).getText()
        article = soup.find("div", {"class": "text-formatted"}).getText()

        return {
            "content": chapo + "\n" + article
        }
