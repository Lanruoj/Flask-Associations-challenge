from flask import Blueprint, jsonify, request, abort
from main import db
from models.users import User
from schemas.user_schema import user_schema
from datetime import timedelta
from main import bcrypt
from flask_jwt_extended import create_access_token

auth = Blueprint('auth', __name__, url_prefix="/auth")

@auth.route("/signup", methods=["POST"])
def auth_signup():
    user_fields = user_schema.load(request.json)
    user = User.query.filter_by(username=user_fields["username"]).first()

    if user:
        return abort(400, description="Username already registered")
        
    user = User()
    user.username = user_fields["username"]
    user.password = bcrypt.generate_password_hash(user_fields["password"]).decode("utf-8")

    db.session.add(user)
    db.session.commit()

    expiry = timedelta(days=1)
    access_token = create_access_token(identity=str(user.id), expires_delta=expiry)
    
    return jsonify({"token": access_token })

@auth.route("/signin", methods=["POST"])
def auth_sigin():
    user_fields = user_schema.load(request.json)
    
    user = User.query.filter_by(username=user_fields["username"]).first()
    # there is not a user with that email or if the password is no correct send an error
    if not user or not bcrypt.check_password_hash(user.password, user_fields["password"]):
        return abort(401, description="Incorrect username and password")
    
    expiry = timedelta(days=1)
    access_token = create_access_token(identity=str(user.id), expires_delta=expiry)

    return jsonify({"token": access_token })