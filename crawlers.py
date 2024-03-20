import urllib3


def crawl_link(url):
    http = urllib3.PoolManager()
    request = http.request("GET", url, headers={'User-Agent': 'Mozilla/5.0'})
    if request.status == 200:
        return request.data

    return ""

