from peewee import Model, CharField, ForeignKeyField


def migrate(migrator, database, fake=False, **kwargs):

    class User(Model):
        pass

    @migrator.create_model
    class Image(Model):

        name = CharField(null=True)
        url = CharField(unique=True)
        owner = ForeignKeyField(User, backref='images')

def rollback(migrator, database, fake=False, **kwargs):
    migrator.remove_model('image')
