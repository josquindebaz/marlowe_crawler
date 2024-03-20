from bs4 import BeautifulSoup


def get_rss_soup(rss_feed):
    rss_soup = BeautifulSoup(rss_feed, 'xml')

    return {
        "description": rss_soup.find("description").getText(),
        "articles": rss_soup.findAll("item"),
    }
