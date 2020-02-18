from peewee import CharField, ForeignKeyField

from models import BaseModel
from models.user import User


class Image(BaseModel):

    name = CharField(null=True)
    url = CharField(unique=True)
    owner = ForeignKeyField(User, backref='images')
