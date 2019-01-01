import requests
from urllib.parse import urljoin

class QuranTafseer:
    web_api_url = 'http://api.quran-tafseer.com/'

    @classmethod
    def get_tafseer_books(self) -> dict:
        """
        Gets the list of avalaible tafseer
        :returns: List of dictionary contains list of tafseer book
        :raises ValueError: raise Value error if the JSON return form the services is invalid.
        :raises Timeout: if the server didn't return any response.
        :raises HTTPError: if the server returned unsuccessful resposne.
        """
        request_url = urljoin(self.web_api_url, 'tafseer')
        response = requests.get(request_url)
        response.raise_for_status()
        return response.json()