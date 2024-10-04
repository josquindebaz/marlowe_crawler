import time

import database
from crawlers import crawl_link
from rss_parser import get_rss_soup


class Controller:
    def __init__(self, rss_links, parser, author):
        self.rss_links = rss_links
        self.parser = parser
        self.author = author

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
                            f'{self.author} -> found {len(rss["articles"])} new articles')

    def get_items_content(self):
        for rss_stream in self.items_from_rss:
            self.parser.process_articles(rss_stream, self.author)
            self.articles.extend(self.parser.articles)
            self.log.append(f'{time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime())}: '
                            f'{self.author} -> crawled {len(self.parser.articles)} articles')

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

        print("\n".join(self.log))
