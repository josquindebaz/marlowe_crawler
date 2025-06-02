from parsers.BaseParser import BaseParser


class AgoravoxParser(BaseParser):
    def parse_article_soup(self, soup):
        article_div = soup.find("div", {"class", "cadretexte"})
        paragraphs = [paragraph.getText() for paragraph in article_div.findAll("p")]

        return {
            "content": "\n".join(paragraphs)
        }
