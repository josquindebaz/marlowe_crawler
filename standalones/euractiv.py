from Controller import Controller
from parsers.EuractivParser import EuractivParser

if __name__ == "__main__":
    controller = Controller(
        rss_links=[
            'https://www.euractiv.fr/sections/international/feed',
            'https://www.euractiv.fr/sections/economie/feed',
            'https://www.euractiv.fr/sections/energie-climat/feed',
            'https://www.euractiv.fr/sections/sante/feed',
            'https://www.euractiv.fr/sections/politique/feed',
        ],
        parser=EuractivParser(),
        author="Euractiv"
    )
    controller.run()

    print(controller.articles)

