from parsers.BaseParser import BaseParser


class RtlAfpParser(BaseParser):
    def parse_article_soup(self, soup):
        return {
            "content": soup.find("div", {"class": "article-body"}).getText()
        }
