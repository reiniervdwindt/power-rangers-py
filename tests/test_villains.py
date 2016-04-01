import unittest

from power_rangers import villains
from power_rangers.errors import NotFoundException


class VillainsTestCase(unittest.TestCase):
    def test_get_villain_by_id(self):
        villain = villains.get_by_id(id=1)

        self.assertIn('id', villain)
        self.assertEqual(villain['id'], 1)

        self.assertIn('name', villain)
        self.assertEqual(villain['name'], 'Rita Repulsa')

        self.assertIn('description', villain)
        self.assertRegexpMatches(villain['description'], '^Rita Repulsa is an evil humanoid alien witch')

        self.assertIn('images', villain)
        self.assertIsInstance(villain['images'], list)

    def test_get_villain_missing_id(self):
        with self.assertRaises(TypeError):
            villains.get_by_id()

    def test_get_villain_not_found(self):
        with self.assertRaises(NotFoundException):
            villains.get_by_id(id=999)


if __name__ == '__main__':
    unittest.main()
