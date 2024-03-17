from . import db

class Property(db.Model):
    __tablename__ = "properties"

    id = db.Column(db.Integer, primary_key=True)
    proptitle = db.Column(db.String(100))
    description = db.Column(db.String(1024))
    number_of_rooms = db.Column(db.Integer)
    price = db.Column(db.Integer)
    location = db.Column(db.String(100))
    photo = db.Column(db.String(255))
    number_of_bathrooms = db.Column(db.Integer)
    property_type = db.Column(db.String(25))

    def __init__(self, proptitle, description, number_of_rooms, price, location, photo, number_of_bathrooms, property_type):
        self.proptitle = proptitle
        self.description = description
        self.number_of_rooms = number_of_rooms
        self.price = price
        self.location = location
        self.photo = photo
        self.number_of_bathrooms = number_of_bathrooms
        self.property_type = property_type

    def __repr__(self):
        return f'<Property {self.id}>'