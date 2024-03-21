from parsers.BaseParser import BaseParser


class FranceInfoParser(BaseParser):
    def parse_article_soup(self, soup):
        result = soup.find("div", {"class": "c-body"})
        if not result:
            return {"content": ""}

        return {
            "content": result.getText()
        }
