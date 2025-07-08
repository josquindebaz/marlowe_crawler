from parsers.BaseParser import BaseParser


class EuronewsParser(BaseParser):
    def parse_article_soup(self, soup):
        chapo = soup.find("meta", {"name": "description"})["content"]

        article = soup.find("div", {"class": "c-article-content"})
        paragraphs = [
            paragraph.getText() for paragraph in article.findAll("p")
        ]

        return {
            "content": chapo + "\n" + "\n".join(paragraphs),
        }
