import unittest

from power_rangers.models import fields
from power_rangers.models.rangers import Ranger


class FieldTestCase(unittest.TestCase):
    def test_base_field(self):
        field = fields.BaseField()
        field.populate('Red Ranger')
        self.assertEqual(field.to_python(), 'Red Ranger')

    def test_char_field(self):
        field = fields.CharField()
        field.populate('Red Ranger')
        self.assertEqual(field.to_python(), 'Red Ranger')

    def test_char_field_no_data(self):
        field = fields.CharField()
        field.populate(data=None)
        self.assertEqual(field.to_python(), None)

    def test_integer_field(self):
        field = fields.IntegerField()
        field.populate(1)
        self.assertEqual(field.to_python(), 1)

    def test_integer_field_no_data(self):
        field = fields.IntegerField()
        field.populate(data=None)
        self.assertEqual(field.to_python(), None)

    def test_float_field(self):
        field = fields.FloatField()
        field.populate(1.0)
        self.assertEqual(field.to_python(), 1.0)

    def test_float_field_no_data(self):
        field = fields.FloatField()
        field.populate(data=None)
        self.assertEqual(field.to_python(), None)

    def test_boolean_field(self):
        field = fields.BooleanField()
        field.populate(True)
        self.assertEqual(field.to_python(), True)

    def test_boolean_field_boolean_string(self):
        field = fields.BooleanField()
        field.populate('true')
        self.assertEqual(field.to_python(), True)

    def test_boolean_field_other(self):
        field = fields.BooleanField()
        field.populate(['ranger'])
        self.assertEqual(field.to_python(), True)

    def test_model_field(self):
        field = fields.ModelField(Ranger)
        field.populate(dict(id=1, name='White Ranger'))

        ranger = field.to_python()
        self.assertEqual(ranger.id, 1)
        self.assertEqual(ranger.name, 'White Ranger')

    def test_model_field_instance(self):
        field = fields.ModelField(Ranger)
        field.populate(Ranger(dict(id=1, name='White Ranger')))

        ranger = field.to_python()
        self.assertEqual(ranger.id, 1)
        self.assertEqual(ranger.name, 'White Ranger')

    def test_model_collection_field(self):
        field = fields.ModelCollectionField(Ranger)
        field.populate([dict(id=1, name='Red Ranger'), dict(id=2, name='White Ranger')])

        rangers = field.to_python()
        self.assertIsInstance(rangers, list)

        ranger = rangers[0]
        self.assertEqual(ranger.id, 1)
        self.assertEqual(ranger.name, 'Red Ranger')

    def test_field_collection_field(self):
        field = fields.FieldCollectionField(fields.CharField)
        field.populate(['Red Ranger', 'Blue Ranger', 'White Ranger'])
        self.assertEqual(field.to_python(), [u'Red Ranger', u'Blue Ranger', u'White Ranger'])
