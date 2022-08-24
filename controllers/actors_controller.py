from flask import Blueprint, jsonify, request, abort
from main import db
from models.actors import Actor
from models.users import User
from schemas.actor_schema import actor_schema, actors_schema
from schemas.role_schema import role_schema, roles_schema
from models.roles import Role
from datetime import date
from flask_jwt_extended import jwt_required, get_jwt_identity

actors = Blueprint('actors', __name__, url_prefix="/actors")


# The GET routes endpoint
@actors.route("/", methods=["GET"])
def get_actors():
    actors_list = Actor.query.all()
    result = actors_schema.dump(actors_list)
    return jsonify(result)


@actors.route("/<int:id>", methods=["GET"])
@jwt_required()
def search_actor(id):
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    if not user:
        return abort(401, description="Invalid user")

    actor = Actor.query.get(id)
    result = actor_schema.dump(actor)
    return jsonify(result)


@actors.route("/", methods=["POST"])
@jwt_required()
def actor_create():
    actor_fields = actor_schema.load(request.json)

    new_actor = Actor()
    new_actor.first_name = actor_fields["first_name"]
    new_actor.last_name = actor_fields["last_name"]
    new_actor.country = actor_fields["country"]
    new_actor.gender = actor_fields["gender"]

    db.session.add(new_actor)
    db.session.commit()
    
    return jsonify(actor_schema.dump(new_actor))

@actors.route("/<int:id>", methods=["DELETE"])
@jwt_required()
def actor_delete(id):
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    if not user:
        return abort(401, description="Invalid user")
        
    actor = Actor.query.filter_by(id=id).first()
    
    if not Actor:
        return abort(400, description= "Actor not found in the db")

    db.session.delete(actor)
    db.session.commit()
    
    return jsonify(actor_schema.dump(actor))


@actors.route("/<int:id>/role", methods=["POST"])
@jwt_required()
def add_role(id):
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    if not user:
        return abort(401, description="Invalid user")
    
    actor = Actor.query.get(id)
    if not actor:
        return abort(400, description="Invalid actor")

    role_fields = role_schema.load(request.json)
    role = Role(
        actor_id = actor.id,
        movie_id = role_fields["movie_id"]
    )
    db.session.add(role)
    db.session.commit()

    return jsonify(role_schema.dump(role))