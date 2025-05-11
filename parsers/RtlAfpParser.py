from parsers.BaseParser import BaseParser


class RtlAfpParser(BaseParser):
    def parse_article_soup(self, soup):
        article = soup.find("div", {"class": "article-body"})

        description = article.find("p", {"class": "article-body__summary"})

        paragraphs = [
            paragraph.getText() for paragraph in soup.findAll("p", class_=False)
        ]

        return {
            "content": "\n".join(paragraphs),
            "description": description.getText()
        }
