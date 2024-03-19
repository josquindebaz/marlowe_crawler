from datetime import datetime
from bs4 import BeautifulSoup

import database
from models.Article import Article
from crawlers import crawl_link
from rss_parser import get_rss_soup


def extract_rss_item_data(info):
    return {
        "link": info.find("link").getText(),
        "date": datetime.strptime(info.find("pubDate").getText(), "%a, %d %b %Y %H:%M:%S %z"),
        "title": info.find("title").getText(),
        "description": info.find("description").getText(),
    }


def get_info_soup(link):
    return BeautifulSoup(crawl_link(link), 'lxml')


def parse_info_soup(soup):
    return {
        "content": soup.find("div", {"class": "c-body"}).getText()
    }


def info_crawler(info):
    """ From title description pubDate link enclosure
        To Article
    """
    info_data = extract_rss_item_data(info)
    info_soup = get_info_soup(info_data["link"])
    parsed_info = parse_info_soup(info_soup)

    return Article(
        date=info_data["date"],
        link=info_data["link"],
        title=info_data["title"],
        description=info_data["description"],
        content=parsed_info["content"],
        author="franceinfo"
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
        rss_content = get_rss_soup(crawl_link(rss_link))
        articles = [info_crawler(item) for item in rss_content["articles"]]

        print(rss_content["description"], " -> crawled ", len(articles), " on ", len(rss_content["articles"]))

        for article in articles:
            print(f"Inserting {article.title}")
            database.insert_in_table(article)
