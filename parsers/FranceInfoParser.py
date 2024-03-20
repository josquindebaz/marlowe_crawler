from parsers.AbstractParser import AbstractParser


class FranceInfoParser(AbstractParser):
    def parse_article_soup(self, soup):
        result = soup.find("div", {"class": "c-body"})
        if not result:
            return {"content": ""}

        return {
            "content": result.getText()
        }
