from flask import Flask, redirect, render_template
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm

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

@app.route('/add', methods=["POST", "GET"])
def add():
    """ Pet add form """

    form = AddPetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data
        available = form.available.data

        pet = Pet(name=name, species=species, photo_url=photo_url, age=age, notes=notes, available=available)

        db.session.add(pet)
        db.session.commit()

        return redirect("/")
    
    else:
        return render_template("add.html", form=form)
    
@app.route('/<int:pet_id>', methods=["POST", "GET"])
def pet(pet_id):
    """ Pet edit form """

    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data

        db.session.commit()

        return redirect("/")
    
    else:
        return render_template("pet.html", form=form, pet=pet)