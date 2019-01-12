from urllib.parse import urljoin

import requests

from .settings import WEB_API_URL


class QuranTafseer:
    @classmethod
    def get_tafseer_books(self, language='') -> list:
        """get_tafseer_books Gets the list of avalaible tafseer

        :param language: filter the list of tafseer based on lanugage,
        defaults to ''
        :param language: str, optional
        :raises ValueError: raise Value error if the JSON return form the
        services is invalid.
        :raises Timeout: if the server didn't return any response.
        :raises HTTPError: if the server returned unsuccessful resposne.
        :return: list of dictonart with tafseer attbutes ['id', 'name',
        'language', 'author', 'book_name']
        :rtype: list
        """
        params = {}
        if language:
            params['lang'] = language
        request_url = urljoin(WEB_API_URL, 'tafseer')
        response = requests.get(request_url, params=params)
        response.raise_for_status()
        return response.json()

    def __init__(self, book_id: int):
        self.book_id = book_id

    def get_tafseer_text(self, chapter_number: int, verse_number: int,
                         verse_number_to: int = None) -> dict:
        """get_tafseer_text Gets the tafseer text for one verse or range of verses

        :param chapter_number: Chapter number
        :param verse_number: Verse number or a start range.
        :param verse_number_to: Verse number end range, defaults to None,
        optional
        """
        request_url = (f'{WEB_API_URL}/tafseer/{self.book_id}/'
                       f'{chapter_number}/{verse_number}')
        if verse_number_to is not None:
            request_url += f'/{verse_number_to}'
        response = requests.get(request_url)
        response.raise_for_status
        return response.json()
