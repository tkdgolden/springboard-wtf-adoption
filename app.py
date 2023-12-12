from flask import Flask, render_template
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pawtential_companions'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)


connect_db(app)
app.app_context().push()
db.create_all()

@app.route('/')
def index():
    """ Homepage shows list of pets """

    pets = Pet.query.all()

    return render_template("index.html", pets=pets)