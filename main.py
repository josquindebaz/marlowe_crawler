from Controller import Controller
from parsers.ActualitesNewsEnvironnementParser import ActualitesNewsEnvironnementParser
from parsers.BfmTvParser import BfmTvParser
from parsers.EuractivParser import EuractivParser
from parsers.France24Parser import France24Parser
from parsers.FranceInfoParser import FranceInfoParser
from parsers.RtlAfpParser import RtlAfpParser
from parsers.lemondeParser import LeMondeParser

if __name__ == "__main__":
    franceinfo_controller = Controller(
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
    franceinfo_controller.run()

    france24_controller = Controller(
        rss_links=[
            'https://www.france24.com/fr/rss'
        ],
        parser=France24Parser(),
        author="france24"
    )
    france24_controller.run()

    bfmtv_controller = Controller(
        rss_links=[
            "https://www.bfmtv.com/rss/sante/",
            "https://www.bfmtv.com/rss/international/",
            "https://www.bfmtv.com/rss/politique/",
            "https://www.bfmtv.com/rss/environnement/",
            "https://www.bfmtv.com/rss/environnement/climat/",
            "https://www.bfmtv.com/rss/international/europe/",
        ],
        parser=BfmTvParser(),
        author="bfmtv"
    )
    bfmtv_controller.run()

    afp_controller = Controller(
        rss_links=[
            "https://infos.rtl.lu/rss/monde",
        ],
        parser=RtlAfpParser(),
        author="afp"
    )
    afp_controller.run()

    euractiv_controller = Controller(
        rss_links=[
            'https://www.euractiv.fr/sections/international/feed',
            'https://www.euractiv.fr/sections/economie/feed',
            'https://www.euractiv.fr/sections/energie-climat/feed',
            'https://www.euractiv.fr/sections/sante/feed',
            'https://www.euractiv.fr/sections/politique/feed',
        ],
        parser=EuractivParser(),
        author='Euractiv'
    )
    euractiv_controller.run()

    lemonde_controller = Controller(
        rss_links=[
            "https://www.lemonde.fr/politique/rss_full.xml",
            "https://www.lemonde.fr/societe/rss_full.xml",
            "https://www.lemonde.fr/les-decodeurs/rss_full.xml",
            "https://www.lemonde.fr/international/rss_full.xml",
            "https://www.lemonde.fr/sante/rss_full.xml",
            "https://www.lemonde.fr/planete/rss_full.xml",
            "https://www.lemonde.fr/politique/rss_full.xml",
            "https://www.lemonde.fr/afrique-climat-et-environnement/rss_full.xml",
            "https://www.lemonde.fr/editoriaux/rss_full.xml",
            "https://www.lemonde.fr/chroniques/rss_full.xml",
            "https://www.lemonde.fr/tribunes/rss_full.xml",
        ],
        parser=LeMondeParser(),
        author="Le Monde"
    )
    lemonde_controller.run()

    actualites_new_environnement_controller = Controller(        rss_links = [
            'https://www.actualites-news-environnement.com/rss.php'
        ],
        parser = ActualitesNewsEnvironnementParser(),
        author = "Actualités news environnement",
    )
    actualites_new_environnement_controller.run()
