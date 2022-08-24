from main import ma
from marshmallow import fields


class DirectorSchema(ma.Schema):
    class Meta:
        ordered = True
        fields = ("id", "first_name", "last_name", "movies")

    movies = fields.List(fields.Nested("MovieSchema"))


director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)