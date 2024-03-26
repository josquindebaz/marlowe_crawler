from bs4 import BeautifulSoup
from datetime import datetime

import database
from models.Article import Article
from crawlers import crawl_link
from parsers.France24Parser import France24Parser
from rss_parser import get_rss_soup


def info_crawler(info):
    """ From title description pubDate link enclosure
        To Article
    """
    link = info.find("link").getText()
    info_soup = BeautifulSoup(crawl_link(link), 'lxml')

    paragraphs = [
        paragraph.getText() for paragraph in info_soup.findAll("p")
        if paragraph.attrs == {}
    ]

    return Article(
        date=datetime.strptime(info.find("pubDate").getText(), "%a, %d %b %Y %H:%M:%S %Z"),
        link=link,
        title=info.find("title").getText(),
        description=info.find("description").getText(),
        content="\n".join(paragraphs),
        author="france24"
    )


if __name__ == "__main__":
    rss_link = "https://www.france24.com/fr/rss"
    rss_content = get_rss_soup(crawl_link(rss_link))

    parser = France24Parser()
    parser.process_articles(rss_content, "france24")

    print("France24", rss_content["description"], " -> crawled ", len(parser.articles),
          " on ", len(rss_content["articles"]))

    for article in parser.articles:
        # print(f"Inserting {article.title}")
        database.insert_in_table(article)
