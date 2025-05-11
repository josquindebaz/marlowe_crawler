from Controller import Controller
from parsers.BaseParser import BaseParser

if __name__ == "__main__":
    controller = Controller(
        rss_links = [
            'https://example.com/rss'   #Replace me
        ],
        parser = BaseParser(),          #Replace me
        author = "db_author_name",      #Replace me
        use_db = False
    )
    controller.run()

    print(controller.articles)
