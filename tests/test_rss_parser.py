from rss_parser import get_rss_soup


def test_get_rss_soup():
    expected_item = ("<item><title>title</title><description>description</description><pubDate>Tue, 19 Mar 2024 "
                     "09:07:52 +0100</pubDate><link>https://www.francetvinfo.fr/monde/russie/vladimir-poutine"
                     "/presidentielle-en-russie-jusqu-ou-peut-aller-vladimir-poutine_6433624.html#xtor=RSS-3-["
                     "general]</link></item>")

    rss_feed = ('<?xml version="1.0"?><rss xmlns:content="http://purl.org/rss/1.0/modules/content/" version="2.0" '
                'xmlns:media="http://search.yahoo.com/mrss/" xmlns:atom="http://www.w3.org/2005/Atom" '
                'xmlns:schema="https://schema.org"><channel><title>Franceinfo- Monde</title><description>Franceinfo- '
                'Monde</description><link>https://www.francetvinfo.fr/monde/</link><pubDate>Tue, 19 Mar 2024 09:09:56 '
                '+0100</pubDate><generator>francetvinfo 2024 (https://www.francetvinfo.fr)</generator><atom:link '
                'rel="self" type="application/rss+xml" href="https://www.francetvinfo.fr/monde.rss"/>%s</channel></rss>'
                % expected_item)

    result = get_rss_soup(rss_feed)

    assert result["description"] == 'Franceinfo- Monde'
    assert len(result["articles"]) == 1
    assert str(result["articles"][0]) in expected_item
