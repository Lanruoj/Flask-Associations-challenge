from main import ma
from marshmallow.validate import Length
from marshmallow import fields


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        ordered = True
        fields = ["id", "username", "password"]
    password = ma.String(validate=Length(min=8))


user_schema = UserSchema()
users_schema = UserSchema(many=True)