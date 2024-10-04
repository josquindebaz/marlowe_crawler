from Controller import Controller
from parsers.France24Parser import France24Parser

if __name__ == "__main__":
    controller = Controller(
        rss_links=[
            'https://www.france24.com/fr/rss'
        ],
        parser=France24Parser(),
        author="france24"
    )
    controller.run()

    print(controller.articles)
