from main import db


class Role(db.Model):
    __tablename__ = "roles"

    id = db.Column(db.Integer, primary_key=True)
    actor_id = db.Column(db.Integer, db.ForeignKey("actors.id"))
    movie_id = db.Column(db.Integer, db.ForeignKey("movies.id"))