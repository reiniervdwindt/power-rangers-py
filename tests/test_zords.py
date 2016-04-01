import unittest

from power_rangers import zords
from power_rangers.errors import NotFoundException


class ZordsTestCase(unittest.TestCase):
    def test_get_zord_by_id(self):
        zord = zords.get_by_id(id=1)

        self.assertIn('id', zord)
        self.assertEqual(zord['id'], 1)

        self.assertIn('name', zord)
        self.assertEqual(zord['name'], 'Tyrannosaurus Dinozord')

        self.assertIn('description', zord)
        self.assertRegexpMatches(zord['description'], '^Forming the head and torso')

        self.assertIn('type', zord)
        self.assertEqual(zord['type'], 'dinozord')

        self.assertIn('images', zord)
        self.assertIsInstance(zord['images'], list)

    def test_get_zord_missing_id(self):
        with self.assertRaises(TypeError):
            zords.get_by_id()

    def test_get_zord_not_found(self):
        with self.assertRaises(NotFoundException):
            zords.get_by_id(id=999)


if __name__ == '__main__':
    unittest.main()
