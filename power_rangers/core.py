import json
import requests

from power_rangers import errors

BASE_URL = 'http://powerapi.blueyes.nl/v1/'


class Core(object):
    def __init__(self):
        # Get all of our exceptions except the base exception
        errs = [getattr(errors, att) for att in errors.__all__ if att != 'PowerRangersException']

        # Map HTTP response codes to exception types
        self.error_map = {err.http_code: err for err in errs}

    @staticmethod
    def _get_url(f, *args, **kwargs):
        generator = f(*args, **kwargs)
        uri = next(generator)
        return BASE_URL + uri, generator

    def _handle_request(self, method, url):
        response = requests.request(method, url)
        if response.status_code in self.error_map:
            raise self.error_map[response.status_code]()
        json_data = json.loads(response.content.decode('UTF-8', 'ignore'))
        return json_data

    def get(self, f):
        def inner(*args, **kwargs):
            resp = self._get_url(f, *args, **kwargs)
            url, generator = resp
            json_data = self._handle_request('get', url)
            return generator.send(json_data)

        return inner


core = Core()
get = core.get
