from parsers.BaseParser import BaseParser


class A20minutesParser(BaseParser):
    def parse_article_soup(self, soup):
        article = (soup.find("div", {"class": "c-content"}))

        return {
            "content": article.getText(),
        }
