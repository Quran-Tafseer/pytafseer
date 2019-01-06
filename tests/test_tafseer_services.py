from tafseer_package.services import QuranTafseer
import pytest


@pytest.mark.vcr()
def test_get_tafseer_books():
    tafseer_list = QuranTafseer.get_tafseer_books()
    assert tafseer_list is not None
    assert list(tafseer_list[0].keys()) == ['id', 'name', 'language', 'author',
                                            'book_name']


@pytest.mark.vcr()
def test_get_tafseer_books_with_lang():
    tafseer_list = QuranTafseer.get_tafseer_books()
    tafseer_list_with_lang = QuranTafseer.get_tafseer_books(language='ar')
    assert len(tafseer_list) > len(tafseer_list_with_lang)
