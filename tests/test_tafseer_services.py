from tafseer_package.services import QuranTafseer
import pytest


def test_get_tafseer_books():
    tafseer_list = QuranTafseer.get_tafseer_books()
    assert tafseer_list is not None
    assert list(tafseer_list[0].keys()) == ['id', 'name', 'language', 'author', 'book_name']
