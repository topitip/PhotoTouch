from marshmallow import Schema, fields


class LoginSchema(Schema):

    phone = fields.String(required=True, max_length=11)
    password = fields.String(required=True)


class RegisterSchema(Schema): 

    first_name = fields.String(required=True)
    surname = fields.String(required=True)
    password = fields.String(required=True)
    phone = fields.String(unique=True, max_length=11)


class UserUpdateSchema(Schema):
    password = fields.String()

    class Meta:
        type_ = "user"


class UserPublicSchema(Schema):

    id = fields.Integer()
    first_name = fields.String()
    surname = fields.String()
    phone = fields.String()

    class Meta:
        type_ = "user"
