from flask import Blueprint, jsonify, request, abort
from main import db
from models.movies import Movie
from models.users import User
from schemas.movie_schema import movie_schema, movies_schema
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
    
    if not Movie:
        return abort(400, description= "Movie not found in the database")

    db.session.delete(movie)
    db.session.commit()
    
    return jsonify(movie_schema.dump(movie))