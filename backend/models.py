#db models

from config import db

class Contact(db.Model):
    #define fields
    id = db.Column(db.Integer, primary_key=True)
    first_name=db.Column(db.String(80),unique=False,nullable=False)#max80chars
    last_name=db.Column(db.String(80),unique=False,nullable=False)
    email=db.Column(db.String(120),unique=True,nullable=False)

    def to_json(self):
        return {
            "id":self.id,
            "firstName":self.first_name,
            "lastName":self.last_name,
            "email":self.email,
        }
    #^function will take
    #all of the different fields that we have
    #on our object here and convert it into a
    #python dictionary which we can then
    #convert into Json which is something we
    #can pass from our API so when we build an API
