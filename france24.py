from bs4 import BeautifulSoup
from datetime import datetime

import database
from models.Article import Article
from crawlers import crawl_link, get_rss


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
    rss_content = get_rss(rss_link)

    articles = [info_crawler(item) for item in rss_content["articles"]]

    print("France 24 -> crawled ", len(articles), " on ", len(rss_content["articles"]))

    for article in articles:
        # print(f"Inserting {article.title}")
        database.insert_in_table(article)
