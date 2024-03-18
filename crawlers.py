import urllib3
from bs4 import BeautifulSoup


def crawl_link(url):
    http = urllib3.PoolManager()
    request = http.request("GET", url, headers={'User-Agent': 'Mozilla/5.0'})
    if request.status == 200:
        return request.data

    return ""


def get_rss(url):
    rss_soup = BeautifulSoup(crawl_link(url), 'xml')

    return {
        "description": rss_soup.find("description").getText(),
        "articles": rss_soup.findAll("item"),
    }
