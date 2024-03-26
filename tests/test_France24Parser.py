from datetime import datetime
from bs4 import BeautifulSoup
from dateutil.tz import tzutc

from models.Article import Article
from parsers.France24Parser import France24Parser
from rss_parser import get_rss_soup


def test_extract_rss_item_data():
    expected = {
        "link": "https://www.france24.com/fr/europe/20240326-attentat-de-moscou-pourquoi-le-kremlin-met-en-sc%C3%A8ne"
                "-sa-brutalit%C3%A9-contre-les-suspect",
        'date': datetime(2024, 3, 26, 16, 46, 32, tzinfo=tzutc()),
        "title": "Attentat de Moscou : pourquoi le Kremlin met en scène sa brutalité contre les suspects",
        "description": "Images et vidéos chocs montrant les brutalités commises contre les suspects de l’attentat "
                       "terroriste à Moscou circulent largement dans les médias et sur les réseaux sociaux en Russie "
                       "ces deux derniers jours. Une manière pour le pouvoir russe de soigner son image d'État "
                       "\"fort\" en faisant fi des critiques dénonçant son recours à la torture.",
    }

    item = (f"<item><category>Europe</category><title>{expected['title']}</title><link>{expected['link']}</link"
            f"><description>{expected['description']}</description><pubDate>Tue, 26 Mar 2024 16:46:32 "
            f"GMT</pubDate></item>")

    rss_feed = ("""<?xml version="1.0" encoding="UTF-8"?><rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom" 
    xmlns:media="http://search.yahoo.com/mrss/" xmlns:dc="http://purl.org/dc/elements/1.1/"><channel><title><![CDATA[ 
    France 24 - Infos, news & actualités - L'information internationale en direct]]></title> <description>France 24 
    décrypte l’actualité internationale, politique, l’économie, l’environnement, la culture, le sport, en France et à 
    l’international avec analyses, des interviews, des reportages exclusifs, des magazines et des 
    documentaires.</description><link>https://www.france24.com/fr/</link><lastBuildDate>Tue, 26 Mar 2024 16:59:45 
    GMT</lastBuildDate><atom:link href="https://www.france24.com/fr/rss" ref="self" 
    type="application/rss+xml"/>%s<language>fr</language></channel></rss>""" % item)

    feed_soup = get_rss_soup(rss_feed)
    parser = France24Parser()
    result = parser.extract_rss_item_data(feed_soup["articles"][0])
    assert result == expected


def test_parse_article_soup():
    text = [
        "Muhammadsobir Fayzov est arrivé en chaise roulante et les yeux fermés dans la salle d’audience à Moscou, "
        "dimanche 24 mars. Saidakrami Rachabalizoda a comparu avec un énorme bandage couvrant son oreille. Un "
        "troisième, Dalerjon Mirzoyev, s’est présenté devant les juges avec un sac plastique autour du cou et des "
        "traces de coupures sur le visage.",
        "Tous trois, ainsi qu’un quatrième individu au visage également tuméfié, sont accusés d’avoir participé à "
        "l’attentat terroriste qui a endeuillé la Russie vendredi 22 mars. Au moins 139 personnes ont péri lors de "
        "cette attaque visant une salle de concert moscovite, le Crocus City Hall. Un attentat sanglant, "
        "le plus meurtrier sur le sol européen revendiqué par l’organisation terroriste État islamiste"]

    html = f"""<p>{text[0]}</p><p>{text[1]}</p>"""

    expected = {"content": "\n".join(text)}

    soup = BeautifulSoup(html, 'lxml')
    parser = France24Parser()
    result = parser.parse_article_soup(soup)

    assert result['content'] == expected['content']


def test_format_article():
    expected = Article(
        link="https://www.bfmtv.com/sante/30-ans-du-sidaction-pourquoi-le-preservatif-est-encore-largement"
             "-delaisse-chez-les-jeunes_AV-202403220844.html",
        date=datetime(2024, 3, 26, 16, 46, 32, tzinfo=tzutc()),
        title="Attentat de Moscou : pourquoi le Kremlin met en scène sa brutalité contre les suspects",
        description="Images et vidéos chocs montrant les brutalités commises contre les suspects de l’attentat "
                    "terroriste à Moscou circulent largement dans les médias et sur les réseaux sociaux en Russie ces "
                    "deux derniers jours. Une manière pour le pouvoir russe de soigner son image d'État \"fort\" en "
                    "faisant fi des critiques dénonçant son recours à la torture.",
        content="Some content",
        author="france24"
    )

    parsed_article = {"content": "Some content"}
    metadata = {
        "link": "https://www.bfmtv.com/sante/30-ans-du-sidaction-pourquoi-le-preservatif-est-encore-largement"
                "-delaisse-chez-les-jeunes_AV-202403220844.html",
        'date': datetime(2024, 3, 26, 16, 46, 32, tzinfo=tzutc()),
        "title": "Attentat de Moscou : pourquoi le Kremlin met en scène sa brutalité contre les suspects",
        "description": "Images et vidéos chocs montrant les brutalités commises contre les suspects de l’attentat "
                       "terroriste à Moscou circulent largement dans les médias et sur les réseaux sociaux en Russie "
                       "ces deux derniers jours. Une manière pour le pouvoir russe de soigner son image d'État "
                       "\"fort\" en faisant fi des critiques dénonçant son recours à la torture."
    }
    parser = France24Parser()
    result = parser.format_article(parsed_article, metadata, author="france24")

    assert result == expected
