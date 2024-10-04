from Controller import Controller
from parsers.FranceInfoParser import FranceInfoParser

if __name__ == "__main__":
    controller = Controller(
        rss_links=[
            'https://www.francetvinfo.fr/politique.rss',
            'https://www.francetvinfo.fr/societe.rss',
            'https://www.francetvinfo.fr/faits-divers.rss',
            'https://www.francetvinfo.fr/sante.rss',
            'https://www.francetvinfo.fr/economie/tendances.rss',
            'https://www.francetvinfo.fr/monde.rss'
        ],
        parser=FranceInfoParser(),
        author="franceinfo"
    )
    controller.run()

    print(controller.articles)
