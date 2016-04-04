class BaseField(object):
    def __init__(self, source=None):
        self.source = source
        self.data = None

    def populate(self, data):
        self.data = data

    def to_python(self):
        return self.data


class CharField(BaseField):
    def to_python(self):
        if self.data:
            return str(self.data)
        return None


class IntegerField(BaseField):
    def to_python(self):
        if self.data:
            return int(self.data)
        return None


class FloatField(BaseField):
    def to_python(self):
        if self.data:
            return float(self.data)
        return None


class BooleanField(BaseField):
    def to_python(self):
        if isinstance(self.data, str):
            return self.data.strip().lower() == 'true'
        if isinstance(self.data, int):
            return self.data > 0
        return bool(self.data)


class WrappedObjectField(BaseField):
    def __init__(self, wrapped_class, **kwargs):
        self._wrapped_class = wrapped_class
        super(WrappedObjectField, self).__init__(**kwargs)


class ModelField(WrappedObjectField):
    def to_python(self):
        if isinstance(self.data, self._wrapped_class):
            return self.data
        else:
            return self._wrapped_class(self.data or {})


class ModelCollectionField(WrappedObjectField):
    def to_python(self):
        return [self._wrapped_class(item) for item in self.data]


class FieldCollectionField(BaseField):
    def __init__(self, field_instance, **kwargs):
        super(FieldCollectionField, self).__init__(**kwargs)
        self._instance = field_instance()

    def to_python(self):
        def convert(item):
            self._instance.populate(item)
            return self._instance.to_python()

        return [convert(item) for item in self.data or []]
