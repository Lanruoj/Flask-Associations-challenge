from main import db
from flask import Blueprint
from main import bcrypt
from models.actors import Actor
from models.movies import Movie
from models.users import User
from datetime import date

db_commands = Blueprint("db", __name__)

# create app's cli command named create, then run it in the terminal as "flask create", 
# it will invoke create_db function
@db_commands .cli.command("create")
def create_db():
    db.create_all()
    print("Tables created")

@db_commands .cli.command("seed")
def seed_db():
    user = User(
        username = "tomato",
        password = bcrypt.generate_password_hash("password123").decode("utf-8")
    )
    db.session.add(user)

    movie1 = Movie(
        title = "Spider-Man: No Way Home",
        genre = "Action",
        length = 148,
        year = 2021
    )
    db.session.add(movie1)

    movie2 = Movie(
        title = "Dune",
        genre = "Sci-fi",
        length = 155,
        year = 2021
    )
    db.session.add(movie2)

    actor1 = Actor(
        first_name = "Tom",
        last_name = "Holland",
        gender = "male",
        country = "UK"
    )
    db.session.add(actor1)

    actor2 = Actor(
        first_name = "Marisa",
        last_name = "Tomei",
        gender = "female",
        country = "USA"
    )
    db.session.add(actor2)

    actor3 = Actor(
        first_name = "Timothee",
        last_name = "Chalemet",
        gender = "male",
        country = "USA"
    )
    db.session.add(actor3)

    actor4 = Actor(
        first_name = "Zendaya",
        last_name = "",
        gender = "female",
        country = "USA"
    )
    db.session.add(actor4)

    # commit the changes
    db.session.commit()
    print("Table seeded") 

@db_commands .cli.command("drop")
def drop_db():
    db.drop_all()
    print("Tables dropped") 