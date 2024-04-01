import database

from crawlers import crawl_link
from parsers.RtlAfpParser import RtlAfpParser
from rss_parser import get_rss_soup


if __name__ == "__main__":
    rss_link = "https://infos.rtl.lu/rss/monde"
    rss_content = get_rss_soup(crawl_link(rss_link))

    parser = RtlAfpParser()
    parser.process_articles(rss_content, "afp")

    print("RTL-AFP", rss_content["description"], " -> crawled ", len(parser.articles),
          " on ", len(rss_content["articles"]))

    for article in parser.articles:
        # print(f"Inserting {article.title}")
        database.insert_in_table(article)
