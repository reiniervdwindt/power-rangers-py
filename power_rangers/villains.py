from power_rangers.core import get
from power_rangers.models import Villain


@get
def get_all():
    data = yield 'villains'

    villains = []
    for villain in data:
        villains.append(Villain(villain))

    yield villains


@get
def get_by_id(villain_id):
    if not isinstance(villain_id, int):
        raise ValueError('id must be an integer')

    data = yield 'villains/{id}'.format(id=villain_id)
    yield Villain(data)
