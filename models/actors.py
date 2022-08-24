from main import db

class Actor(db.Model):
    # define the table name for the db
    __tablename__= "actors"
    # Set the primary key, we need to define that each attribute is also a column in the db table, remember "db" is the object we created in the previous step.
    id = db.Column(db.Integer,primary_key=True)  
    first_name = db.Column(db.String())
    last_name = db.Column(db.String())
    gender = db.Column(db.String())
    country = db.Column(db.String())

    roles = db.relationship(
        "Role",
        cascade="all, delete"
    )

