import random
import urllib3


def crawl_link(url):
    http = urllib3.PoolManager()
    request = http.request("GET", url)
    if request.status == 200:
        return request.data

    return ""

