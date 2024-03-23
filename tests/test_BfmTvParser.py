from datetime import datetime, timezone, timedelta

from bs4 import BeautifulSoup

from models.Article import Article
from parsers.BfmTvParser import BfmTvParser
from rss_parser import get_rss_soup


def test_extract_rss_item_data():
    expected = {
        "link": "https://www.bfmtv.com/sante/30-ans-du-sidaction-pourquoi-le-preservatif-est-encore-largement"
                "-delaisse-chez-les-jeunes_AV-202403220844.html",
        'date': datetime(2024, 3, 22, 20, 22, 28),
        "title": "30 ans du Sidaction: pourquoi le préservatif est encore largement délaissé chez les jeunes",
        "description": "Malgré la gratuité de certains préservatifs pour les jeunes de moins de 26 ans depuis 2023, "
                       "la mesure est méconnue puisque seulement 5% des concernés disent l'avoir demandé, "
                       "selon une récente enquête.",
    }

    item = (
        f"<item><title>{expected['title']}</title><description>{expected['description']}</description><pubDate>Fri, "
        f"22 Mar 2024 20:22:28 GMT</pubDate><link>{expected['link']}</link></item>")

    rss_feed = ("""<?xml version="1.0" encoding="utf-8"?> <rss version="2.0" 
    xmlns:atom="http://www.w3.org/2005/Atom"> <channel> <title>Home Santé - actualités</title> 
    <link>https://www.bfmtv.com/sante/</link> <description>Retrouvez toute l'actualité santé et sujets de société: 
    santé connectée et publique, obésité, régime, articles, guides et vidéos conseils pour rester en bonne 
    santé</description> <lastBuildDate>Sat, 23 Mar 2024 07:15:25 GMT</lastBuildDate> 
    <docs>http://blogs.law.harvard.edu/tech/rss</docs> <generator>BFMTV</generator> <language>fr</language> <image> 
    <title>Home Santé - actualités</title> 
    <url>https://www.bfmtv.com/assets/v4/images/BFMTV_default_16x9.8715a163008e9f3fc3799c8e2c6ebafa.jpg</url> 
    <link>https://www.bfmtv.com/sante/</link> </image> <copyright>Copyright BFMTV</copyright> <category>Home Santé - 
    actualités</category> <atom:link href="https://www.bfmtv.com/sante/" rel="self" type="application/rss+xml"/> 
    %s</channel> </rss>""" % item)

    feed_soup = get_rss_soup(rss_feed)
    parser = BfmTvParser()
    result = parser.extract_rss_item_data(feed_soup["articles"][0])

    assert result == expected


def test_parse_article_soup():
    description = "Malgré la gratuité de certains préservatifs"
    text = [
        "Un outil indispensable pour lutter contre le VIH, mais délaissé par les plus jeunes. 30 ans après sa création",
        "pour les jeunes de moins de 26 ans, la mesure est méconnue."]

    html = f"""<div class="chapo">{description}</div>
    <p>{text[0]}</p><p>{text[1]}</p>
    <p>unwanted content</p><p>unwanted content</p><p>unwanted content</p>
    """

    expected = {"content": "\n".join(text),
                "description": description}

    soup = BeautifulSoup(html, 'lxml')

    parser = BfmTvParser()
    result = parser.parse_article_soup(soup)

    assert result['description'] == expected['description']
    assert result['content'] == expected['content']


def test_format_article():
    expected = Article(
        link="https://www.bfmtv.com/sante/30-ans-du-sidaction-pourquoi-le-preservatif-est-encore-largement"
             "-delaisse-chez-les-jeunes_AV-202403220844.html",
        date=datetime(2024, 3, 22, 20, 22, 28),
        title="30 ans du Sidaction: pourquoi le préservatif est encore largement délaissé chez les jeunes",
        description="Malgré la gratuité de certains préservatifs pour les jeunes de moins de 26 ans depuis 2023",
        content="Some content",
        author="bfmtv"
    )

    parsed_article = {"content": "Some content",
                      "description": "Malgré la gratuité de certains préservatifs pour les jeunes de moins de 26 ans "
                                     "depuis 2023",}
    metadata = {
        "link": "https://www.bfmtv.com/sante/30-ans-du-sidaction-pourquoi-le-preservatif-est-encore-largement"
                "-delaisse-chez-les-jeunes_AV-202403220844.html",
        'date': datetime(2024, 3, 22, 20, 22, 28),
        "title": "30 ans du Sidaction: pourquoi le préservatif est encore largement délaissé chez les jeunes",
        "description": "Some article description",
    }
    parser = BfmTvParser()
    result = parser.format_article(parsed_article, metadata, author="bfmtv")

    assert result == expected
