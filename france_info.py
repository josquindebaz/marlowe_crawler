import database

from crawlers import crawl_link
from parsers.FranceInfoParser import FranceInfoParser
from rss_parser import get_rss_soup

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
        parser = FranceInfoParser()
        parser.process_articles(rss_content, "franceinfo")

        print(rss_content["description"], " -> crawled ", len(parser.articles), " on ", len(rss_content["articles"]))

        for article in parser.articles:
            # print(f"Inserting {article.title}")
            database.insert_in_table(article)
