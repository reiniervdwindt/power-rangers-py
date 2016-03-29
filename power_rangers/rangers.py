from core import get


@get
def get_by_id(id):
    if not isinstance(id, int):
        raise ValueError('id must be an integer')

    data = yield 'rangers/{id}'.format(id=id)
    yield data
