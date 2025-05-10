from Controller import Controller
from parsers.lemondeParser import LeMondeParser

if __name__ == "__main__":
    controller = Controller(
        rss_links=[
            "https://www.lemonde.fr/rss/une.xml",
            "https://www.lemonde.fr/international/rss_full.xml",
            "https://www.lemonde.fr/sante/rss_full.xml",
            "https://www.lemonde.fr/planete/rss_full.xml",
            "https://www.lemonde.fr/politique/rss_full.xml",
            "https://www.lemonde.fr/afrique-climat-et-environnement/rss_full.xml"
        ],
        parser=LeMondeParser(),
        author="Le Monde"
    )
    controller.run()

    # print(controller.articles)
