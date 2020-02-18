from peewee import Model, Field

from libs.peewee import database


class BaseModel(Model):
    class Meta:
        database = database


class EnumField(Field):
    field_type = 'integer'

    def __init__(self, enum: list):
        super().__init__()
        self.enum = enum

    def db_value(self, value):
        return self.enum.index(value) + 1

    def python_value(self, value):
        if value < len(self.enum) + 1:
            return self.enum[value - 1]
        else:
            return None
