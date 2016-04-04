import unittest

from six import assertRegex

from power_rangers import zords
from power_rangers.errors import NotFoundException
from power_rangers.models.zords import Zord
from tests.mock import Mock


class ZordsTestCase(unittest.TestCase):
    def test_get_zords(self):
        with Mock('zords/list.json'):
            response = zords.get_all()

            self.assertIsInstance(response, list)
            self.assertGreaterEqual(len(response), 1)

            zord = response[0]
            self.assertIsInstance(zord, Zord)
            self.assertEqual(zord.name, 'Dino Megazord')

    def test_get_zord_by_id(self):
        with Mock('zords/get.json'):
            zord = zords.get_by_id(18)

            self.assertIsInstance(zord, Zord)
            self.assertEqual(zord.id, 18)
            self.assertEqual(zord.name, 'White Tigerzord')
            self.assertEqual(zord.type, 'thunderzord')
            self.assertIsInstance(zord.images, list)

            assertRegex(self, zord.description, '^With the creation of the White Power Ranger')

    def test_get_zord_missing_id(self):
        with self.assertRaises(TypeError):
            zords.get_by_id()

    def test_get_zord_wrong_id_type(self):
        with self.assertRaises(ValueError):
            zords.get_by_id('megazord')

    def test_get_zord_not_found(self):
        with Mock('errors/notfound.json', status=404):
            with self.assertRaises(NotFoundException):
                zords.get_by_id(999)
