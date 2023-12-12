from models import db, Pet

db.drop_all()
db.create_all()

Pet.query.delete()

orange = Pet(name="Orange", species="Dog", photo_url="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e7/06101298_Grand_anglo_francais_orange.jpg/330px-06101298_Grand_anglo_francais_orange.jpg", age=1, notes="weird toungue in picture but he looks much more normal I promise.", available=True)
english = Pet(name="English", species="Dog", photo_url="https://upload.wikimedia.org/wikipedia/commons/thumb/7/7c/%22Bill%22_-_Cocker_spaniel_anglais_2.JPG/330px-%22Bill%22_-_Cocker_spaniel_anglais_2.JPG", age=2, notes="so regal", available=True)
hamilton = Pet(name="Hamilton", species="Dog", photo_url="https://upload.wikimedia.org/wikipedia/commons/thumb/5/52/Hamiltonstovare_600.jpg/330px-Hamiltonstovare_600.jpg", age=3, notes="Handsome, upstanding dog of striking colouring. Hardy and sound. Rectangular, well proportioned, giving impression of great strength and stamina. Tricoloured.", available=False)
showa = Pet(name="Showa Sanke", species="Fish", photo_url="https://upload.wikimedia.org/wikipedia/commons/thumb/5/56/Showa4.JPG/800px-Showa4.JPG", age=4, notes="a really big, expensive goldfish", available=True)
ronald = Pet(name="Ronald", species="Bird", photo_url="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Peacock_by_Nihal_jabin.jpg/330px-Peacock_by_Nihal_jabin.jpg", age=5)
ugly = Pet(name="The Ugly Duckling", species="Bird", photo_url="https://upload.wikimedia.org/wikipedia/commons/thumb/1/19/Cairina_moschata_momelanotus_head.jpg/330px-Cairina_moschata_momelanotus_head.jpg", age=6, notes="https://upload.wikimedia.org/wikipedia/commons/thumb/1/19/Cairina_moschata_momelanotus_head.jpg/330px-Cairina_moschata_momelanotus_head.jpg", available=False)
itty = Pet(name="itty", species="Fish")

db.session.add(orange)
db.session.add(english)
db.session.add(hamilton)
db.session.add(showa)
db.session.add(ronald)
db.session.add(ugly)
db.session.add(itty)

db.session.commit()