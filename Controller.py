import time

import database
from crawlers import crawl_link
from rss_parser import get_rss_soup


class Controller:
    def __init__(self, rss_links, parser, author):
        self._rss_links = rss_links
        self._parser = parser
        self._author = author

        self._items_from_rss = []
        self._log = []

        self.articles = []

    def get_items_from_rss(self):
        self._items_from_rss = []

        for rss_link in self._rss_links:
            rss = get_rss_soup(crawl_link(rss_link))

            rss["articles"] = [
                item for item in rss["articles"]
                if not database.is_in_table(item.find("link").getText())
            ]

            self._items_from_rss.append(rss)
            self._log.append(f'{time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.localtime())}: '
                             f'{self._author} -> found {len(rss["articles"])} new articles')

    def get_items_content(self):
        for rss_stream in self._items_from_rss:
            self._parser.process_articles(rss_stream, self._author)
            self.articles.extend(self._parser.articles)
            self._log.append(f'{time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime())}: '
                             f'{self._author} -> crawled {len(self._parser.articles)} articles')

    def store(self):
        insert_count = 0
        for article in self.articles:
            insert_count += database.insert_in_table(article)

        self._log.append(f'{time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.localtime())}: '
                         f'{self._author} inserted {insert_count} on {len(self.articles)}')

    def run(self):
        self.get_items_from_rss()
        self.get_items_content()
        self.store()

        print("\n".join(self._log))
