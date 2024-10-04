from Controller import Controller
from parsers.RtlAfpParser import RtlAfpParser

if __name__ == "__main__":
    controller = Controller(
        rss_links=[
            "https://infos.rtl.lu/rss/monde",
        ],
        parser=RtlAfpParser(),
        author="afp"
    )
    controller.run()

    print(controller.articles)
