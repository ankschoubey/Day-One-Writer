from datetime import datetime

class Entry:
    text: str = ''
    tags: list = []
    date: datetime = None
    photos: list = []
    journal: str = None
    starred: bool = False
    coordinate: list = []
    timezone: list = None