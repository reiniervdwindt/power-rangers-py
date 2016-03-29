import unittest

from power_rangers import villains
from power_rangers.errors import NotFoundException


class TestVillains(unittest.TestCase):
    def test_get_villain_by_id(self):
        villain = villains.get_by_id(id=1)
        self.assertEqual(villain['name'], 'Rita Repulsa')
        self.assertIn('description', villain)

    def test_get_villain_missing_id(self):
        with self.assertRaises(TypeError):
            villains.get_by_id()

    def test_get_villain_not_found(self):
        with self.assertRaises(NotFoundException):
            villains.get_by_id(id=999)
