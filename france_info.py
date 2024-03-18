from datetime import datetime
from bs4 import BeautifulSoup

import database
from Article import Article
from crawlers import crawl_link, get_rss


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
        content=info_soup.find("div", {"class": "c-body"}).getText()
    )


if __name__ == "__main__":
    rss_links = [
        'https://www.francetvinfo.fr/politique.rss',
        'https://www.francetvinfo.fr/societe.rss',
        'https://www.francetvinfo.fr/faits-divers.rss',
        'https://www.francetvinfo.fr/sante.rss',
        'https://www.francetvinfo.fr/economie/tendances.rss',
        'https://www.francetvinfo.fr/monde.rss'
    ]

    for rss_link in rss_links:
        rss_content = get_rss(rss_link)
        articles = [info_crawler(item) for item in rss_content["articles"]]

        print(rss_content["description"], " -> crawled ", len(articles), " on ", len(rss_content["articles"]))

        for article in articles:
            print(f"Inserting {article.title}")
            database.insert_in_table(article)
