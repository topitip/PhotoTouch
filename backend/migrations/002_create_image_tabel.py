from peewee import (
    Model, CharField,
    ForeignKeyField, IntegerField
)
from playhouse.postgres_ext import ArrayField

def migrate(migrator, database, fake=False, **kwargs):

    class User(Model):
        pass

    @migrator.create_model
    class Image(Model):

        name = CharField(null=True)
        url = CharField(unique=True)
        owner_id = ForeignKeyField(User, backref='images')
        users = ArrayField(IntegerField)

def rollback(migrator, database, fake=False, **kwargs):
    migrator.remove_model('image')
