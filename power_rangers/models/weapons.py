from . import fields
from .base import Image, Model


class Ranger(Model):
    id = fields.IntegerField()
    name = fields.CharField()
    color = fields.CharField()


class Weapon(Model):
    id = fields.IntegerField()
    name = fields.CharField()
    type = fields.CharField()
    ranger = fields.ModelField(Ranger)
    images = fields.ModelCollectionField(Image)
