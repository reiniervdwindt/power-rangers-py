from . import fields
from .base import Image, Model


class Weapon(Model):
    id = fields.IntegerField()
    name = fields.CharField()
    type = fields.CharField()


class Zord(Model):
    id = fields.IntegerField()
    name = fields.CharField()
    description = fields.CharField()
    type = fields.CharField


class Ranger(Model):
    id = fields.IntegerField()
    name = fields.CharField()
    color = fields.CharField()
    weapon = fields.ModelField(Weapon)
    zords = fields.ModelCollectionField(Zord)
    images = fields.ModelCollectionField(Image)
