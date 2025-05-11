from datetime import datetime, timezone, timedelta
from dateutil.tz import tzutc

from parsers.BaseParser import BaseParser
from rss_parser import get_rss_soup


def test_extract_france_info_rss_item_data():
    expected = {
        "link": "https://www.francetvinfo.fr/monde/russie/vladimir-poutine/presidentielle-en-russie-jusqu-ou-peut"
                "-aller-vladimir-poutine_6433624.html",
        'date': datetime(2024, 3, 19, 9, 7, 52, tzinfo=timezone(timedelta(seconds=3600))),
        "title": "A title",
        "description": "Some article description",
    }

    item = (
        f"<item><title>{expected['title']}</title><description>{expected['description']}</description><pubDate>Tue, "
        f"19 Mar 2024 09:07:52 +0100</pubDate><link>{expected['link']}</link></item>")

    rss_feed = ('<?xml version="1.0"?><rss xmlns:content="http://purl.org/rss/1.0/modules/content/" version="2.0" '
                'xmlns:media="http://search.yahoo.com/mrss/" xmlns:atom="http://www.w3.org/2005/Atom" '
                'xmlns:schema="https://schema.org"><channel><title>Franceinfo- Monde</title><description>Franceinfo- '
                'Monde</description><link>https://www.francetvinfo.fr/monde/</link><pubDate>Tue, 19 Mar 2024 09:09:56 '
                '+0100</pubDate><generator>francetvinfo 2024 (https://www.francetvinfo.fr)</generator><atom:link '
                'rel="self" type="application/rss+xml" href="https://www.francetvinfo.fr/monde.rss"/>%s</channel></rss>'
                % item)

    feed_soup = get_rss_soup(rss_feed)
    parser = BaseParser()
    result = parser.extract_rss_item_data(feed_soup["articles"][0])

    assert result == expected


def test_extract_bfmtv_rss_item_data():
    expected = {
        "link": "https://www.bfmtv.com/sante/30-ans-du-sidaction-pourquoi-le-preservatif-est-encore-largement"
                "-delaisse-chez-les-jeunes_AV-202403220844.html",
        'date': datetime(2024, 3, 22, 20, 22, 28, tzinfo=tzutc()),
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
    parser = BaseParser()
    result = parser.extract_rss_item_data(feed_soup["articles"][0])

    assert result == expected
