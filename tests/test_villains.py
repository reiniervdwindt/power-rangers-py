import unittest

from six import assertRegex

from power_rangers import villains
from power_rangers.errors import NotFoundException
from power_rangers.models.villains import Villain
from tests.mock import Mock


class VillainsTestCase(unittest.TestCase):
    def test_get_villains(self):
        with Mock('villains/list.json'):
            response = villains.get_all()

            self.assertIsInstance(response, list)
            self.assertGreaterEqual(len(response), 1)

            villain = response[0]
            self.assertIsInstance(villain, Villain)
            self.assertEqual(villain.name, 'Goldar')

    def test_get_villain_by_id(self):
        with Mock('villains/get.json'):
            villain = villains.get_by_id(1)

            self.assertIsInstance(villain, Villain)
            self.assertEqual(villain.id, 1)
            self.assertEqual(villain.name, 'Rita Repulsa')
            self.assertIsInstance(villain.images, list)

            assertRegex(self, villain.description, '^Rita Repulsa is an evil humanoid alien witch')

    def test_get_villain_missing_id(self):
        with self.assertRaises(TypeError):
            villains.get_by_id()

    def test_get_villains_wrong_id_type(self):
        with self.assertRaises(ValueError):
            villains.get_by_id('rita')

    def test_get_villain_not_found(self):
        with Mock('errors/notfound.json', status=404):
            with self.assertRaises(NotFoundException):
                villains.get_by_id(999)
