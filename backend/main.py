#main routes and endpoints(localhost:5000/createcontact<-endpoint)
#CRUD app

#create
# - first_name
# - last_name
# - email

from flask import request,jsonify
from config import app, db
from models import Contact

@app.route("/contacts",methods=["GET"]) #decorator
def get_contacts():
    contacts = Contact.query.all() #getting all diff contacts
    #need to convert python objects from python to json
    json_contacts = list(map(lambda x:x.to_json(),contacts))
    return jsonify({"contacts":json_contacts}) #json reply,200 status by default

@app.route("/create_contact",methods=["POST"])
def create_contact():
    first_name = request.json.get("firstName")
    last_name = request.json.get("lastName")
    email = request.json.get("email")

    if not first_name or not last_name or not email:
        return(
            jsonify({"message": "You must include a first name, last name and email"}),
            400,
        )
    
    new_contact = Contact(first_name=first_name,last_name=last_name,email=email)
    try:
        db.session.add(new_contact)#in staging area
        db.session.commit()
    except Exception as e:
        return jsonify({"message":str(e)}),400
    
    return jsonify({"message":"User created!"}),201

@app.route("/update_contact/<int:user_id>", methods=["PATCH"])#user id to be updated. path parameter
def update_contact(user_id):
    contact = Contact.query.get(user_id) #checking if user exists
    #                           ^id from path 
    if not contact:
        return jsonify({"message":"User not found"}),404
    
    data = request.json
    contact.first_name = data.get("firstName",contact.first_name) 
    #if "firstName" exists update it, else keep it the same^
    contact.last_name = data.get("lastName",contact.last_name) 
    contact.email = data.get("email",contact.email) 
    #added in session (staged)

    db.session.commit()

    return jsonify({"message": "User updated."}), 200

@app.route("/delete_contact/<int:user_id>",methods=["DELETE"])
def delete_contact(user_id):
    contact = Contact.query.get(user_id) #checking if user exists

    if not contact:
        return jsonify({"message":"User deleted!"}),404
    
    db.session.delete(contact)
    db.session.commit()

    return jsonify({"message": "User deleted!"}),200

if __name__ == "__main__": #run only if not just importing object etc
    with app.app_context():
        db.create_all() #create all of the different models defined in db

    app.run(debug=True)