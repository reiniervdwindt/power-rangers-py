import unittest

from power_rangers import rangers
from power_rangers.errors import NotFoundException


class TestRangers(unittest.TestCase):
    def test_get_ranger_by_id(self):
        ranger = rangers.get_by_id(id=1)
        self.assertEqual(ranger['name'], 'Red Ranger')
        self.assertEqual(ranger['color'], 'red')

    def test_get_ranger_missing_id(self):
        with self.assertRaises(TypeError):
            rangers.get_by_id()

    def test_get_ranger_not_found(self):
        with self.assertRaises(NotFoundException):
            rangers.get_by_id(id=999)
