import time

import database

from crawlers import crawl_link
from parsers.FranceInfoParser import FranceInfoParser
from rss_parser import get_rss_soup


class FranceInfoController:
    def __init__(self):
        self.rss_links = [
            'https://www.francetvinfo.fr/politique.rss',
            'https://www.francetvinfo.fr/societe.rss',
            'https://www.francetvinfo.fr/faits-divers.rss',
            'https://www.francetvinfo.fr/sante.rss',
            'https://www.francetvinfo.fr/economie/tendances.rss',
            'https://www.francetvinfo.fr/monde.rss'
        ]

        self.items_from_rss = []
        self.articles = []
        self.log = []

    def get_items_from_rss(self):
        self.items_from_rss = []
        for rss_link in self.rss_links:
            rss = get_rss_soup(crawl_link(rss_link))

            rss["articles"] = [
                item for item in rss["articles"]
                if not database.is_in_table(item.find("link").getText())
            ]

            self.items_from_rss.append(rss)
            self.log.append(f'{time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.localtime())}: '
                            f'{rss["description"]} -> found {len(rss["articles"])} new articles')

    def get_items_content(self):
        for rss_stream in self.items_from_rss:
            parser = FranceInfoParser()

            parser.process_articles(rss_stream, "franceinfo")
            self.articles.extend(parser.articles)
            self.log.append(f'{time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime())}: '
                            f'{rss_stream["description"]} -> crawled {len(parser.articles)} articles')

    def store(self):
        for article in self.articles:
            self.log.append(f'{time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.localtime())}: '
                            f'Inserting {article.title}')
            result = database.insert_in_table(article)
            if result != 'ok':
                self.log.append(result)

    def run(self):
        self.get_items_from_rss()
        self.get_items_content()
        self.store()

        # print("\n".join(controller.log))


if __name__ == "__main__":
    controller = FranceInfoController()
    controller.run()
