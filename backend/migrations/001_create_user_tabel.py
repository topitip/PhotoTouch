from peewee import Model, CharField


def migrate(migrator, database, fake=False, **kwargs):

    @migrator.create_model
    class User(Model):

        first_name = CharField()
        surname = CharField()
        password = CharField()
        phone = CharField(unique=True, max_length=11)


def rollback(migrator, database, fake=False, **kwargs):
    migrator.remove_model('user')
