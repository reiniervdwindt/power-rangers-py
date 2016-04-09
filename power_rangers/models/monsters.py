from . import fields
from .base import Image, Model


class Monster(Model):
    id = fields.IntegerField()
    name = fields.CharField()
    description = fields.CharField()
    images = fields.ModelCollectionField(Image)
