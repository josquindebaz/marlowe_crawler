import time

import database
from crawlers import crawl_link
from rss_parser import get_rss_soup


class Controller:
    def __init__(self, rss_links, parser, author, use_db=True):
        self._rss_links = rss_links
        self._parser = parser
        self.author = author
        self._use_db = use_db

        self._items_from_rss = []
        self._log = []

        self.articles = []

    def get_items_from_rss(self):
        self._items_from_rss = []

        for rss_link in self._rss_links:
            rss = get_rss_soup(crawl_link(rss_link))

            rss["articles"] = [
                item for item in rss["articles"]
                if self.is_to_be_crawled(item.find("link").getText())
            ]

            self._items_from_rss.append(rss)
            self._log.append(f'{time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.localtime())}: '
                             f'{self.author} -> found {len(rss["articles"])} new articles')

    def is_to_be_crawled(self, url):
        if not self._use_db:
            return True

        return not database.is_in_table(url)

    def get_items_content(self):
        for rss_stream in self._items_from_rss:
            self._parser.process_articles(rss_stream, self.author)
            self.articles.extend(self._parser.articles)
            self._log.append(f'{time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime())}: '
                             f'{self.author} -> crawled {len(self._parser.articles)} articles')

    def store(self):
        insert_count = 0
        for article in self.articles:
            is_inserted = database.insert_in_table(article)
            if is_inserted:
                insert_count += 1

        self._log.append(f'{time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.localtime())}: '
                         f'{self.author} inserted {insert_count} on {len(self.articles)}')

    def run(self):
        try:
            self.get_items_from_rss()
        except Exception as error:
            self._log.append(f"rss error: {str(error)}")

        try:
            self.get_items_content()
        except Exception as error:
            self._log.append(f"content error: {str(error)}")

        if self._use_db:
            self.store()

        print("\n".join(self._log))
