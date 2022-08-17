from main import ma
from marshmallow.validate import Length
from models.users import User

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        fields = ["id", "username", "password"]
    password = ma.String(validate=Length(min=8))

user_schema = UserSchema()
users_schema = UserSchema(many=True)