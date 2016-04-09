from .core import get
from .models.monsters import Monster


@get
def get_all():
    data = yield 'monsters'

    monsters = []
    for monster in data:
        monsters.append(Monster(monster))

    yield monsters


@get
def get_by_id(monster_id):
    if not isinstance(monster_id, int):
        raise ValueError('id must be an integer')

    data = yield 'monsters/{id}'.format(id=monster_id)
    yield Monster(data)
