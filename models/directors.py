from main import db


class Director(db.Model):
    __tablename__ = "directors"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(), nullable=False)
    last_name = db.Column(db.String(), nullable=False)
    country = db.Column(db.String())

    movies = db.relationship(
        "Movie",
        cascade="all, delete"
    )