import unittest

from power_rangers import monsters
from power_rangers.errors import NotFoundException
from power_rangers.models.monsters import Monster
from tests.mock import Mock


class MonstersTestCase(unittest.TestCase):
    def test_get_monsters(self):
        with Mock('monsters/list.json'):
            response = monsters.get_all()

            self.assertIsInstance(response, list)
            self.assertGreaterEqual(len(response), 1)

            monster = response[0]
            self.assertIsInstance(monster, Monster)
            self.assertEqual(monster.id, 25)
            self.assertEqual(monster.name, 'Babe Ruthless')
            self.assertRegexpMatches(monster.description, '^Babe Ruthless was a one-horned baseball-esque pixie')
            self.assertIsInstance(monster.images, list)

    def test_get_monster_by_id(self):
        with Mock('monsters/get.json'):
            monster = monsters.get_by_id(1)

            self.assertIsInstance(monster, Monster)
            self.assertEqual(monster.id, 1)
            self.assertEqual(monster.name, 'Bones')
            self.assertRegexpMatches(monster.description, '^Bones is a skeleton monster created by Finster')

            self.assertIsInstance(monster.images, list)
            self.assertEqual(len(monster.images), 1)

            image = monster.images[0]
            self.assertEqual(image.url, 'http://powerapi.blueyes.nl/static/media/monsters/MMPR_Bones.jpg')

    def test_get_monster_missing_id(self):
        with self.assertRaises(TypeError):
            monsters.get_by_id()

    def test_get_monster_wrong_id_type(self):
        with self.assertRaises(ValueError):
            monsters.get_by_id('red-monster')

    def test_get_monster_not_found(self):
        with Mock('errors/notfound.json', status=404):
            with self.assertRaises(NotFoundException):
                monsters.get_by_id(999)
