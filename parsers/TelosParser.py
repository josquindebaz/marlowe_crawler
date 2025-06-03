from parsers.BaseParser import BaseParser


class TelosParser(BaseParser):
    def parse_article_soup(self, soup):
        article = soup.find("article")
        authors = article.find("ul", {"class": "authors"})
        authors = [author.getText() for author in authors.find_all("li")]

        article.find("h1").decompose()
        article.find("header").decompose()
        for div in article.findAll("div"):
            div.decompose()

        return {
            "content": article.getText() + " ".join(authors)
        }
