from controllers.actors_controller import actors
from controllers.movies_controller import movies
from controllers.auth_controller import auth

registerable_controllers = [
    auth,
    actors,
    movies
]