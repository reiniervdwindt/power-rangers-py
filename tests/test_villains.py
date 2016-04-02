import unittest

from power_rangers import villains
from power_rangers.errors import NotFoundException
from power_rangers.models import Villain


class VillainsTestCase(unittest.TestCase):
    def test_get_villains(self):
        response = villains.get_all()

        self.assertIsInstance(response, list)
        self.assertGreaterEqual(len(response), 1)

        villain = response[0]
        self.assertIsInstance(villain, Villain)
        self.assertEqual(villain.name, 'Rita Repulsa')

    def test_get_villain_by_id(self):
        villain = villains.get_by_id(1)

        self.assertIsInstance(villain, Villain)
        self.assertEqual(villain.id, 1)
        self.assertEqual(villain.name, 'Rita Repulsa')
        self.assertRegexpMatches(villain.description, '^Rita Repulsa is an evil humanoid alien witch')
        self.assertIsInstance(villain.images, list)

    def test_get_villain_missing_id(self):
        with self.assertRaises(TypeError):
            villains.get_by_id()

    def test_get_villain_not_found(self):
        with self.assertRaises(NotFoundException):
            villains.get_by_id(999)
