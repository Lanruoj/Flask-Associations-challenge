from main import ma
from marshmallow import fields


class MovieSchema(ma.Schema):
    class Meta:
        ordered = True
        fields = ("id", "title", "genre", "length", "year", "director_id", "reviews")

    # director_id = fields.Nested("DirectorSchema")
    reviews = fields.List(fields.Nested("ReviewSchema"), many=True)


movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)