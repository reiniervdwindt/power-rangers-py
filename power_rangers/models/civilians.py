from . import fields
from .base import Image, Model


class Civilian(Model):
    id = fields.IntegerField()
    name = fields.CharField()
    description = fields.CharField()
    images = fields.ModelCollectionField(Image)
