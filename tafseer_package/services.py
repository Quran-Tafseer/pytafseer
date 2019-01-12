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
                         with_verse_text: bool = False) -> dict:
        """get_tafseer_text Gets the tafseer text for one verse or range of verses

        :param chapter_number: Chapter number
        :param verse_number: Verse number or a start range.
        """
        request_url = (f'{WEB_API_URL}/tafseer/{self.book_id}/'
                       f'{chapter_number}/{verse_number}')
        response = requests.get(request_url)
        response.raise_for_status
        tafseer_dict = response.json()
        if with_verse_text:
            verse_text_url = urljoin(WEB_API_URL, tafseer_dict['ayah_url'])
            tafseer_dict['verse_text'] = self._get_verse_text(verse_text_url)
        return tafseer_dict

    def get_tafseer_text_range(self, chapter_number: int,
                               verse_number_from: int,
                               verse_number_to: int,
                               with_verse_text: bool = False) -> dict:
        """get_tafseer_text Gets the tafseer text for one verse or range of verses

        :param chapter_number: Chapter number
        :param verse_number_from: Verse number start range.
        :param verse_number_to: Verse number end range.
        """
        request_url = (f'{WEB_API_URL}/tafseer/{self.book_id}/'
                       f'{chapter_number}/{verse_number_from}/'
                       f'{verse_number_to}')
        response = requests.get(request_url)
        response.raise_for_status
        tafseer_dict = response.json()
        if with_verse_text:
            for verse in tafseer_dict:
                verse_text_url = urljoin(WEB_API_URL, verse['ayah_url'])
                verse['verse_text'] = self._get_verse_text(verse_text_url)
        return tafseer_dict

    def _get_verse_text(self, url: str) -> str:
        """_get_verse_text Gets verse text.

        :param url: URL to make a request to get the verse text
        :return: The verse text
        :rtype: str
        """

        verse_text_url = urljoin(WEB_API_URL, url)
        verse_text_res = requests.get(verse_text_url)
        verse_text_res.raise_for_status
        return verse_text_res.json()['text']
