from peewee import CharField

from models import BaseModel


class User(BaseModel):

    first_name = CharField()
    surname = CharField()
    password = CharField()
    phone = CharField(unique=True, max_length=11)
