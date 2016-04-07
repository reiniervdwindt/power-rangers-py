from collections import OrderedDict

from six import with_metaclass

from . import fields


class MetaModel(type):
    base_fields = None

    def __new__(mcs, name, bases, attrs):
        current_fields = []
        for key, value in list(attrs.items()):
            if isinstance(value, fields.BaseField):
                current_fields.append((key, value))
                attrs.pop(key)
        attrs['declared_fields'] = OrderedDict(current_fields)

        new_class = (super(MetaModel, mcs).__new__(mcs, name, bases, attrs))

        # Walk through the MRO.
        declared_fields = OrderedDict()
        for base in reversed(new_class.__mro__):
            # Collect fields from base class.
            if hasattr(base, 'declared_fields'):
                declared_fields.update(base.declared_fields)

        new_class.base_fields = declared_fields

        return new_class


class Model(with_metaclass(MetaModel)):
    def __init__(self, data):
        self.set_data(data)

    def set_data(self, data=None):
        for name, field in self.base_fields.items():
            key = field.source or name
            if key in data:
                setattr(self, name, data.get(key))

    def __setattr__(self, key, value):
        if key in self.base_fields:
            field = self.base_fields[key]
            field.populate(value)
            super(Model, self).__setattr__(key, field.to_python())


class Image(Model):
    url = fields.CharField(source='image')
