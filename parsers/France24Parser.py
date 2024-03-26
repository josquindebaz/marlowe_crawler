from parsers.BaseParser import BaseParser


class France24Parser(BaseParser):
    def parse_article_soup(self, soup):
        paragraphs = [
            paragraph.getText() for paragraph in soup.findAll("p")
            if paragraph.attrs == {}
        ]

        return {
            "content": "\n".join(paragraphs),
        }

