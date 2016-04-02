from power_rangers.core import get
from power_rangers.models import Weapon


@get
def get_all():
    data = yield 'weapons'

    weapons = []
    for weapon in data:
        weapons.append(Weapon(weapon))

    yield weapons


@get
def get_by_id(weapon_id):
    if not isinstance(weapon_id, int):
        raise ValueError('id must be an integer')

    data = yield 'weapons/{id}'.format(id=weapon_id)
    yield Weapon(data)
