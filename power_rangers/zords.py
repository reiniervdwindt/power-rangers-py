from power_rangers.core import get
from power_rangers.models.zords import Zord


@get
def get_all():
    data = yield 'zords'

    zords = []
    for zord in data:
        zords.append(Zord(zord))

    yield zords


@get
def get_by_id(zord_id):
    if not isinstance(zord_id, int):
        raise ValueError('id must be an integer')

    data = yield 'zords/{id}'.format(id=zord_id)
    yield Zord(data)
