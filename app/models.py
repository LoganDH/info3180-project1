from . import db


class Properties(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250))
    number_of_bedrooms = db.Column(db.String(5))
    number_of_bathrooms = db.Column(db.String(5))
    location = db.Column(db.String(500))
    price = db.Column(db.String(16))
    type = db.Column(db.String(80))
    description = db.Column(db.String(1000))
    photo = db.Column(db.String(250))

    def __init__(self, title, number_of_bedrooms, number_of_bathrooms, location, price, type, description, photo):
        self.title = title
        self.number_of_bedrooms = number_of_bedrooms
        self.number_of_bathrooms = number_of_bathrooms
        self.location = location
        self.price = price
        self.type = type
        self.description = description
        self.photo = photo

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<User %r>' % self.username
