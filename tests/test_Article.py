import dataclasses
from datetime import datetime

from models.Article import Article


def test_create_empty_article():
    expected = {
        "date": None,
        "link": "",
        "title": "",
        "description": "",
        "content": "",
        "author": "",
        "lang": "fr"
    }
    article = Article()

    assert dataclasses.asdict(article) == expected


def test_create_article_with_values():
    expected = {
        "date": datetime.now(),
        "link": "link",
        "title": "title",
        "description": "description",
        "content": "Hello world!",
        "author": "Someone",
        "lang": "fr"
    }

    article = Article(
        date=expected["date"],
        link="link",
        title="title",
        description="description",
        content="Hello world!",
        author="Someone")

    assert dataclasses.asdict(article) == expected
