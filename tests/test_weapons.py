import unittest

from power_rangers import weapons
from power_rangers.errors import NotFoundException
from power_rangers.models import Weapon
from tests.mock import Mock


class WeaponsTestCase(unittest.TestCase):
    def test_get_weapons(self):
        with Mock('weapons/list.json'):
            response = weapons.get_all()

            self.assertIsInstance(response, list)
            self.assertGreaterEqual(len(response), 1)

            weapon = response[0]
            self.assertIsInstance(weapon, Weapon)
            self.assertEqual(weapon.name, 'Dragon Dagger')

    def test_get_weapon_by_id(self):
        with Mock('weapons/get.json'):
            weapon = weapons.get_by_id(1)

            self.assertEqual(weapon.id, 1)
            self.assertEqual(weapon.name, 'Power Sword')
            self.assertEqual(weapon.type, 'sword')
            self.assertIsInstance(weapon.images, list)

    def test_get_weapon_missing_id(self):
        with self.assertRaises(TypeError):
            weapons.get_by_id()

    def test_get_weapon_wrong_id_type(self):
        with self.assertRaises(ValueError):
            weapons.get_by_id('power-sword')

    def test_get_weapon_not_found(self):
        with self.assertRaises(NotFoundException):
            weapons.get_by_id(999)
