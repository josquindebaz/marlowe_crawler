from dataclasses import dataclass
from datetime import datetime


@dataclass
class Article:
    date: datetime = None
    link: str = ""
    title: str = ""
    description: str = ""
    content: str = ""
    author: str = ""
    lang: str = "fr"
