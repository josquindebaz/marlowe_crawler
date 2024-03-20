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

    return Article(
        datetime.strptime(info.find("pubDate").getText(), "%a, %d %b %Y %H:%M:%S %z"),
        link,
        title=info.find("title").getText(),
        description=info.find("description").getText(),
        content=info_soup.find("div", {"class": "article-body"}).getText(),
        author="afp"
    )


if __name__ == "__main__":
    rss_link = "https://infos.rtl.lu/rss/monde"
    rss_content = get_rss_soup(crawl_link(rss_link))
    articles = [info_crawler(item) for item in rss_content["articles"]]

    print("RTL-AFP", rss_content["description"], " -> crawled ", len(articles), " on ", len(rss_content["articles"]))

    for article in articles:
        # print(f"Inserting {article.title}")
        database.insert_in_table(article)
