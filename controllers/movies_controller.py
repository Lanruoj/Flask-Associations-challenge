from flask import Blueprint, jsonify, request, abort
from main import db
from models.movies import Movie
from models.users import User
from schemas.movie_schema import movie_schema, movies_schema
from models.reviews import Review
from schemas.review_schema import review_schema, reviews_schema
from models.directors import Director
from schemas.director_schema import director_schema, directors_schema
from datetime import date
from flask_jwt_extended import jwt_required, get_jwt_identity

movies = Blueprint('movies', __name__, url_prefix="/movies")


@movies.route("/", methods=["GET"])
def get_movies():
    movies_list = Movie.query.all()
    result = movies_schema.dump(movies_list)
    return jsonify(result)

@movies.route("/", methods=["POST"])
@jwt_required()
def movie_create():
    movie_fields = movie_schema.load(request.json)

    new_movie = Movie()
    new_movie.title = movie_fields["title"]
    new_movie.genre = movie_fields["genre"]
    new_movie.length = movie_fields["length"]
    new_movie.year = movie_fields["year"]
    new_movie.director_id = movie_fields["director_id"]

    db.session.add(new_movie)
    db.session.commit()
    
    return jsonify(movie_schema.dump(new_movie))

@movies.route("/<int:id>", methods=["DELETE"])
@jwt_required()
def movie_delete(id):
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    if not user:
        return abort(401, description="Invalid user")
        
    movie = Movie.query.filter_by(id=id).first()
    
    if not movie:
        return abort(400, description= "Movie not found in the database")

    db.session.delete(movie)
    db.session.commit()
    
    return jsonify(movie_schema.dump(movie))


@movies.route("/<int:id>/review", methods=["POST"])
@jwt_required()
def review_add(id):
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    if not user:
        return abort(401, description="Invalid user")
    
    movie = Movie.query.get(id)
    if not movie:
        return abort(400, description="Movie not found")
    
    review_fields = review_schema.load(request.json)
    review = Review(
        title = review_fields["title"],
        message = review_fields["message"],
        date = date.today(),
        user_id = user.id,
        movie_id = movie.id,
    )
    db.session.add(review)
    db.session.commit()
    
    return jsonify(review_schema.dump(review))