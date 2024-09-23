from parsers.BaseParser import BaseParser


class EuractivParser(BaseParser):
    def parse_article_soup(self, soup):
        result = soup.find("div", {"class": "ea-article-body-content"})
        if not result:
            return {"content": ""}

        return {
            "content": result.getText()
        }
