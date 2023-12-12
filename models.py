from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

class Pet(db.Model):
    """ a pet has an id, name, species, photo url, age, notes, and availability """

    __tablename__ = "pets"

    id = db.Column(db.Integer,
                   primary_key = True, 
                   autoincrement = True)
    name = db.Column(db.Text,
                     nullable = False)
    species = db.Column(db.Text,
                        nullable = False)
    photo_url = db.Column(db.Text)
    age = db.Column(db.Integer)
    notes = db.Column(db.Text)
    available = db.Column(db.Boolean,
                          default=True)
    