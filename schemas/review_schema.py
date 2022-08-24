from main import ma
from marshmallow import fields


class ReviewSchema(ma.Schema):
    class Meta:
        ordered = True
        fields = ("id", "title", "message", "date", "user_id", "movie_id")

    user_id = fields.Nested("UserSchema")
    movie_id = fields.Nested("MovieSchema")


review_schema = ReviewSchema()
reviews_schema = ReviewSchema(many=True)