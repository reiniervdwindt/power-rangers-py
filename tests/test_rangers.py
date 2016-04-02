import unittest

from power_rangers import rangers
from power_rangers.errors import NotFoundException
from power_rangers.models import Ranger


class RangersTestCase(unittest.TestCase):
    def test_get_rangers(self):
        response = rangers.get_all()

        self.assertIsInstance(response, list)
        self.assertGreaterEqual(len(response), 1)

        ranger = response[0]
        self.assertIsInstance(ranger, Ranger)
        self.assertEqual(ranger.name, 'Red Ranger')

    def test_get_ranger_by_id(self):
        ranger = rangers.get_by_id(1)

        self.assertIsInstance(ranger, Ranger)
        self.assertEqual(ranger.id, 1)
        self.assertEqual(ranger.name, 'Red Ranger')
        self.assertEqual(ranger.color, 'red')
        self.assertEqual(ranger.weapon, 1)
        self.assertIsInstance(ranger.images, list)

    def test_get_ranger_missing_id(self):
        with self.assertRaises(TypeError):
            rangers.get_by_id()

    def test_get_ranger_not_found(self):
        with self.assertRaises(NotFoundException):
            rangers.get_by_id(999)
