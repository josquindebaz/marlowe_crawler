import database

from crawlers import crawl_link
from parsers.France24Parser import France24Parser
from rss_parser import get_rss_soup

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
