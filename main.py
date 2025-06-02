from Controller import Controller
from parsers.ActualitesNewsEnvironnementParser import ActualitesNewsEnvironnementParser
from parsers.AgoravoxParser import AgoravoxParser
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
        author="franceinfo",
    )

    france24_controller = Controller(
        rss_links=[
            'https://www.france24.com/fr/rss'
        ],
        parser=France24Parser(),
        author="france24",
    )

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
        author="bfmtv",
    )

    afp_controller = Controller(
        rss_links=[
            "https://infos.rtl.lu/rss/monde",
        ],
        parser=RtlAfpParser(),
        author="afp",
    )

    euractiv_controller = Controller(
        rss_links=[
            'https://www.euractiv.fr/sections/agriculture-food/?feed=mcfeed',
            'https://www.euractiv.fr/sections/economy-jobs/?feed=mcfeed',
            'https://www.euractiv.fr/sections/eet/?feed=mcfeed',
            'https://www.euractiv.fr/sections/health-consumers/?feed=mcfeed',
            'https://www.euractiv.fr/sections/politics/?feed=mcfeed',
            'https://www.euractiv.fr/sections/tech/?feed=mcfeed'
        ],
        parser=EuractivParser(),
        author='Euractiv',
    )

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
        author="Le Monde",
    )

    actualites_new_environnement_controller = Controller(
        rss_links=[
            'https://www.actualites-news-environnement.com/rss.php'
        ],
        parser=ActualitesNewsEnvironnementParser(),
        author="Actualités news environnement",
    )

    agoravox_controller = Controller(
        rss_links=[
            "https://www.agoravox.fr/spip.php?page=backend&id_rubrique=35",
            "https://www.agoravox.fr/spip.php?page=backend&id_rubrique=30",
            "https://www.agoravox.fr/spip.php?page=backend&id_rubrique=37",
            "https://www.agoravox.fr/spip.php?page=backend&id_rubrique=29",
            "https://www.agoravox.fr/spip.php?page=backend&id_rubrique=28",
            "https://www.agoravox.fr/spip.php?page=backend&id_rubrique=39",
            "https://www.agoravox.fr/spip.php?page=backend&id_rubrique=33",
            "https://www.agoravox.fr/spip.php?page=backend&id_rubrique=31",
            "https://www.agoravox.fr/spip.php?page=backend&id_rubrique=45",
            "https://www.agoravox.fr/spip.php?page=backend&id_rubrique=36",
            "https://www.agoravox.fr/spip.php?page=backend&id_rubrique=32",
            "https://www.agoravox.fr/spip.php?page=backend&id_rubrique=34"
        ],
        parser=AgoravoxParser(),
        author="Agoravox"
    )

    controller_list = [
        franceinfo_controller,
        france24_controller,
        bfmtv_controller,
        afp_controller,
        euractiv_controller,
        lemonde_controller,
        actualites_new_environnement_controller,
        agoravox_controller
    ]

    for controller in controller_list:
        print("Crawling: ", controller.author)
        controller.run()
