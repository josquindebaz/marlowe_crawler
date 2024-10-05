from Controller import Controller
from parsers.BfmTvParser import BfmTvParser

if __name__ == "__main__":
    controller = Controller(
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
    controller.run()

    print(controller.articles)
