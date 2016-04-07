from . import fields
from .base import Image, Model


class Villain(Model):
    id = fields.IntegerField()
    name = fields.CharField()
    description = fields.CharField()
    images = fields.ModelCollectionField(Image)
