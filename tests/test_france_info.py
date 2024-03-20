from bs4 import BeautifulSoup

from france_info import parse_info_soup


def test_parse_info():
    expected = 'hello world!'
    content = '<div class="c-body">%s</div>' % expected
    soup = BeautifulSoup(content, 'lxml')
    result = parse_info_soup(soup)

    assert result["content"] == expected
