from . import fields
from .base import Image, Model


class ZordMode(Model):
    id = fields.IntegerField()
    name = fields.CharField()
    description = fields.CharField()
    images = fields.ModelCollectionField(Image)


class ZordPart(Model):
    id = fields.IntegerField()
    name = fields.CharField()
    description = fields.CharField()
    type = fields.CharField
    images = fields.ModelCollectionField(Image)


class Zord(Model):
    id = fields.IntegerField()
    name = fields.CharField()
    description = fields.CharField()
    type = fields.CharField()
    images = fields.ModelCollectionField(Image)
    modes = fields.ModelCollectionField(ZordMode)
    parts = fields.ModelCollectionField(ZordPart)
