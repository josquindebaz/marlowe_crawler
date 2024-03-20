from bs4 import BeautifulSoup
from datetime import datetime

import database
from models.Article import Article
from crawlers import crawl_link
from rss_parser import get_rss_soup


def info_crawler(info):
    """ From title description pubDate link enclosure
        To Article
    """
    link = info.find("link").getText()
    info_soup = BeautifulSoup(crawl_link(link), 'lxml')

    paragraphs = [
        paragraph.getText() for paragraph in info_soup.findAll("p")
    ]

    chapo = info_soup.find("div", {"class": "chapo"})
    description = chapo.getText() if chapo else ""

    return Article(
        date=datetime.strptime(info.find("pubDate").getText(), "%a, %d %b %Y %H:%M:%S %Z"),
        link=link,
        title=info.find("title").getText(),
        description=description,
        content="\n".join(paragraphs[:-3]),
        author="bfmtv"
    )


if __name__ == "__main__":
    rss_links = [
        "https://www.bfmtv.com/rss/sante/",
        "https://www.bfmtv.com/rss/international/",
        "https://www.bfmtv.com/rss/politique/",
        "https://www.bfmtv.com/rss/environnement/",
        "https://www.bfmtv.com/rss/environnement/climat/",
        "https://www.bfmtv.com/rss/international/europe/",

    ]

    for rss_link in rss_links:
        rss_content = get_rss_soup(crawl_link(rss_link))

        articles = [info_crawler(item) for item in rss_content["articles"]]
        articles = [article for article in articles if article.content]

        print("bfmtv", rss_content["description"], " -> crawled ", len(articles), " on ", len(rss_content["articles"]))

        for article in articles:
            # print(f"Inserting {article.title} {article.date}")
            database.insert_in_table(article)
