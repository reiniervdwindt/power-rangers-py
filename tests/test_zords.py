import unittest

from power_rangers import zords
from power_rangers.errors import NotFoundException
from power_rangers.models import Zord


class ZordsTestCase(unittest.TestCase):
    def test_get_zords(self):
        response = zords.get_all()

        self.assertIsInstance(response, list)
        self.assertGreaterEqual(len(response), 1)

        zord = response[0]
        self.assertIsInstance(zord, Zord)
        self.assertEqual(zord.name, 'Dino Megazord')

    def test_get_zord_by_id(self):
        zord = zords.get_by_id(1)

        self.assertEqual(zord.id, 1)
        self.assertEqual(zord.name, 'Tyrannosaurus Dinozord')
        self.assertRegexpMatches(zord.description, '^Forming the head and torso')
        self.assertEqual(zord.type, 'dinozord')
        self.assertIsInstance(zord.images, list)

    def test_get_zord_missing_id(self):
        with self.assertRaises(TypeError):
            zords.get_by_id()

    def test_get_zord_not_found(self):
        with self.assertRaises(NotFoundException):
            zords.get_by_id(999)
