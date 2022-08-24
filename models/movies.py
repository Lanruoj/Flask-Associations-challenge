from main import db

class Movie(db.Model):
    # define the table name for the db
    __tablename__= "movies"
    # Set the primary key, we need to define that each attribute is also a column in the db table, remember "db" is the object we created in the previous step.
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String())
    genre = db.Column(db.String())
    length = db.Column(db.Integer())
    year = db.Column(db.Integer())
    director_id = db.Column(db.Integer, db.ForeignKey("directors.id"), nullable=False)

    reviews = db.relationship(
        "Review",
        cascade="all, delete"
    )

