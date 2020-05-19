from typing import NamedTuple, Dict, List


class AnkiDeck(NamedTuple):
    id: int
    name: str
    notes: List = []


class AnkiNote(NamedTuple):
    model: str
    template: str
    data: List = []


class AnkiPackage(NamedTuple):
    filename: str
    deck: AnkiDeck


class AnkiItem(NamedTuple):
    meta: Dict
    data: Dict
