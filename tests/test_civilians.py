import unittest

from power_rangers import civilians
from power_rangers.errors import NotFoundException
from power_rangers.models import Civilian
from tests.mock import Mock


class CiviliansTestCase(unittest.TestCase):
    def test_get_civilians(self):
        with Mock('civilians/list.json'):
            response = civilians.get_all()

            self.assertIsInstance(response, list)
            self.assertGreaterEqual(len(response), 1)

            civilian = response[0]
            self.assertIsInstance(civilian, Civilian)
            self.assertEqual(civilian.id, 6)
            self.assertEqual(civilian.name, 'Angela')
            self.assertRegexpMatches(civilian.description, '^Angela was a minor character')
            self.assertIsInstance(civilian.images, list)

    def test_get_civilian_by_id(self):
        with Mock('civilians/get.json'):
            civilian = civilians.get_by_id(1)

            self.assertIsInstance(civilian, Civilian)
            self.assertEqual(civilian.id, 1)
            self.assertEqual(civilian.name, 'Farkas Bulkmeier')
            self.assertRegexpMatches(civilian.description, '^Farkas "Bulk" Bulkmeier is a fictional character')
            self.assertIsInstance(civilian.images, list)

    def test_get_civilian_missing_id(self):
        with self.assertRaises(TypeError):
            civilians.get_by_id()

    def test_get_civilian_wrong_id_type(self):
        with self.assertRaises(ValueError):
            civilians.get_by_id('red-civilian')

    def test_get_civilian_not_found(self):
        with self.assertRaises(NotFoundException):
            civilians.get_by_id(999)
