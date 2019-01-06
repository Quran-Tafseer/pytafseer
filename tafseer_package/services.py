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
