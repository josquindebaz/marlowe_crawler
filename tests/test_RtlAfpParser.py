from datetime import datetime, timezone, timedelta

from bs4 import BeautifulSoup

from models.Article import Article
from parsers.RtlAfpParser import RtlAfpParser
from rss_parser import get_rss_soup


def test_extract_rss_item_data():
    expected = {
        "link": "https://infos.rtl.lu/actu/monde/a/2181848.html",
        'date': datetime(2024, 3, 28, 6, 7, 36, tzinfo=timezone(timedelta(seconds=3600))),
        "title": "Pont effondré à Baltimore: Les corps de deux des six ouvriers retrouvés",
        "description": "Les corps sans vie de deux des six ouvriers recherchés ont été repêchés mercredi des eaux "
                       "glacées du port de Baltimore, sur la côte Est américaine, ont annoncé les autorités, "
                       "au lendemain de l'effondrement spectaculaire d'un pont percuté par un porte-conteneurs.",
    }

    item = f"""
    <item>
      <title>{expected['title']}</title>
      <description><![CDATA[Les corps sans vie de deux des six ouvriers recherchés ont été repêchés mercredi des eaux glacées du port de Baltimore, sur la côte Est américaine, ont annoncé les autorités, au lendemain de l'effondrement spectaculaire d'un pont percuté par un porte-conteneurs.]]></description>
      <pubDate>Thu, 28 Mar 2024 06:07:36 +0100</pubDate>
      <link>{expected['link']}</link>
      <guid>https://infos.rtl.lu/actu/monde/a/2181848.html</guid>
      <enclosure type="image/jpeg" length="0" url="https://static.rtl.lu/rtl2008.lu/nt/p/2024/03/28/06/ba29c59fbb31574ceb935a4afd66870b.jpeg"/>
      <content:encoded><![CDATA[<img src="https://static.rtl.lu/rtl2008.lu/nt/p/2024/03/28/06/ba29c59fbb31574ceb935a4afd66870b.jpeg" hspace="5" align="left" />Les corps sans vie de deux des six ouvriers recherchés ont été repêchés mercredi des eaux glacées du port de Baltimore, sur la côte Est américaine, ont annoncé les autorités, au lendemain de l'effondrement spectaculaire d'un pont percuté par un porte-conteneurs.]]></content:encoded>
      <slash:comments>0</slash:comments>
    </item>"""

    rss_feed = ("""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom" xmlns:content="http://purl.org/rss/1.0/modules/content/" xmlns:slash="http://purl.org/rss/1.0/modules/slash/">
  <channel>
    <language>fr</language>
    <title>RTL Infos Monde</title>
    <description>Monde</description>
    <image>
      <url>https://static.rtl.lu/rtl/layout/logo_rtl.png</url>
      <title>RTL Infos Monde</title>
      <link>https://infos.rtl.lu/rss/monde</link>
      <description>Monde</description>
    </image>
    <pubDate>Thu, 28 Mar 2024 06:07:36 +0100</pubDate>
    <generator>Laminas_Feed_Writer 2 (https://getlaminas.org)</generator>
    <link>https://infos.rtl.lu/rss/monde</link>
    <copyright>Copyright RTL / CLT-UFA S.A.</copyright>
    <atom:link rel="self" type="application/rss+xml" href="https://infos.rtl.lu/rss/monde"/>%s</channel>
</rss>
    """ % item)

    feed_soup = get_rss_soup(rss_feed)
    parser = RtlAfpParser()
    result = parser.extract_rss_item_data(feed_soup["articles"][0])
    assert result == expected


def test_parse_article_soup():
    expected_chapo = ('Les corps sans vie de deux des six ouvriers recherchés ont été repêchés mercredi des eaux glacées du '
                'port de Baltimore, sur la côte Est américaine, ont annoncé les autorités, au lendemain de '
                'l\'effondrement spectaculaire d\'un pont percuté par un porte-conteneurs.')
    expected_content = 'Lorem Ipsum'
    content = '<div class="article__body article-body"><p class="article-body__summary">%s</p><p>%s</p>' % (
        expected_chapo, expected_content)
    soup = BeautifulSoup(content, 'lxml')

    parser = RtlAfpParser()
    result = parser.parse_article_soup(soup)

    assert result["description"] == expected_chapo
    assert result["content"] == expected_content


def test_format_article():
    expected = Article(
        date=datetime(2024, 3, 28, 6, 7, 36, tzinfo=timezone(timedelta(seconds=3600))),
        link="https://infos.rtl.lu/actu/monde/a/2181848.html",
        title="Pont effondré à Baltimore: Les corps de deux des six ouvriers retrouvés",
        description="Les corps sans vie de deux des six ouvriers recherchés ont été repêchés mercredi des eaux "
                    "glacées du port de Baltimore, sur la côte Est américaine, ont annoncé les autorités, "
                    "au lendemain de l'effondrement spectaculaire d'un pont percuté par un porte-conteneurs.",
        content="Some content",
        author="afp"
    )
    parsed_article = {"content": "Some content"}
    metadata = {
        "link": "https://infos.rtl.lu/actu/monde/a/2181848.html",
        'date': datetime(2024, 3, 28, 6, 7, 36, tzinfo=timezone(timedelta(seconds=3600))),
        "title": "Pont effondré à Baltimore: Les corps de deux des six ouvriers retrouvés",
        "description": "Les corps sans vie de deux des six ouvriers recherchés ont été repêchés mercredi des eaux "
                       "glacées du port de Baltimore, sur la côte Est américaine, ont annoncé les autorités, "
                       "au lendemain de l'effondrement spectaculaire d'un pont percuté par un porte-conteneurs.",
    }
    parser = RtlAfpParser()

    result = parser.format_article(parsed_article, metadata, author="afp")

    assert result == expected
