import unittest

from power_rangers import rangers
from power_rangers.errors import NotFoundException


class RangersTestCase(unittest.TestCase):
    def test_get_ranger_by_id(self):
        ranger = rangers.get_by_id(id=1)

        self.assertIn('id', ranger)
        self.assertEqual(ranger['id'], 1)

        self.assertIn('name', ranger)
        self.assertEqual(ranger['name'], 'Red Ranger')

        self.assertIn('color', ranger)
        self.assertEqual(ranger['color'], 'red')

        self.assertIn('weapon', ranger)
        self.assertEqual(ranger['weapon'], 1)

        self.assertIn('images', ranger)
        self.assertIsInstance(ranger['images'], list)

    def test_get_ranger_missing_id(self):
        with self.assertRaises(TypeError):
            rangers.get_by_id()

    def test_get_ranger_not_found(self):
        with self.assertRaises(NotFoundException):
            rangers.get_by_id(id=999)


if __name__ == '__main__':
    unittest.main()
