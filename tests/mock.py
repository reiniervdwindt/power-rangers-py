from httmock import all_requests, HTTMock
from os.path import dirname


class Mock(HTTMock):
    def __init__(self, filename):
        filepath = '{path}/mock/{filename}'.format(path=dirname(__file__), filename=filename)
        super(Mock, self).__init__(all_requests(lambda url, request: open(filepath).read()))
