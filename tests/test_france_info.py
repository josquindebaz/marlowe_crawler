from bs4 import BeautifulSoup
from datetime import datetime, timezone, timedelta

from france_info import parse_info_soup, extract_rss_item_data
from rss_parser import get_rss_soup


def test_parse_info():
    expected = 'hello world!'
    content = '<div class="c-body">%s</div>' % expected
    soup = BeautifulSoup(content, 'lxml')
    result = parse_info_soup(soup)

    assert result["content"] == expected


def test_extract_rss_item_data():
    expected = {
        "link": "https://www.francetvinfo.fr/monde/russie/vladimir-poutine/presidentielle-en-russie-jusqu-ou-peut"
                "-aller-vladimir-poutine_6433624.html#xtor=RSS-3-[general]",
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
    result = extract_rss_item_data(feed_soup["articles"][0])

    assert result == expected
