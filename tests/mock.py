from os.path import dirname

from httmock import HTTMock, all_requests, response


class Mock(HTTMock):
    def __init__(self, filename, status=200):
        filepath = '{path}/mock/{filename}'.format(path=dirname(__file__), filename=filename)
        with open(filepath) as file:
            content = file.read()
            super(Mock, self).__init__(all_requests(lambda url, request: response(status, content)))
