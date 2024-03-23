import database

from crawlers import crawl_link
from parsers.BfmTvParser import BfmTvParser
from rss_parser import get_rss_soup

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
        parser = BfmTvParser()
        parser.process_articles(rss_content, "bfmtv")

        print("bfmtv", rss_content["description"], " -> crawled ", len(parser.articles),
              " on ", len(rss_content["articles"]))

        for article in parser.articles:
            # print(f"Inserting {article.title} {article.date}")
            database.insert_in_table(article)
