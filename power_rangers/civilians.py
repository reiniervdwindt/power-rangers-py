from power_rangers.core import get
from power_rangers.models import Civilian


@get
def get_all():
    data = yield 'civilians'

    civilians = []
    for civilian in data:
        civilians.append(Civilian(civilian))

    yield civilians


@get
def get_by_id(civilian_id):
    if not isinstance(civilian_id, int):
        raise ValueError('id must be an integer')

    data = yield 'civilians/{id}'.format(id=civilian_id)
    yield Civilian(data)
