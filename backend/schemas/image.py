from marshmallow import Schema, fields

DEFAULT_IMG = '/storage/default/default.png'


class UserNestedSchema(Schema):
    id = fields.Integer()
    first_name = fields.String()
    surname = fields.String()
    title = fields.String()

    class Meta:
        type_ = "user"


class ProjectPublicSchema(Schema):
    id = fields.Integer()
    name = fields.String()
    title = fields.String()
    image = fields.Function(
        lambda obj: obj.images[0].url if obj.images else DEFAULT_IMG
    )

    class Meta:
        type_ = "project"


class ProjectDetailzedSchema(Schema):
    id = fields.Integer()
    name = fields.String()
    title = fields.String()
    description = fields.String()
    started_at = fields.Date()
    ended_at = fields.Date()
    square = fields.Integer()
    images = fields.Function(
        lambda obj: [
            image.url for image in sorted(obj.images, key=lambda img: img.id)
        ]
    )
    users = fields.Nested(UserNestedSchema, many=True)

    class Meta:
        type_ = "project"