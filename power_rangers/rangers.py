from power_rangers.core import get
from power_rangers.models import Ranger


@get
def get_all():
    data = yield 'rangers'

    rangers = []
    for ranger in data:
        rangers.append(Ranger(ranger))

    yield rangers


@get
def get_by_id(ranger_id):
    if not isinstance(ranger_id, int):
        raise ValueError('id must be an integer')

    data = yield 'rangers/{id}'.format(id=ranger_id)
    yield Ranger(data)
