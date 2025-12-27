from flask import request, jsonify
from config import app,db
from models import Contacts

#use something like postman to test your apis

#this is the method that is going to authenticate the users into their accounts
@app.route('/', methods=["POST"])
def auth_user():
    userInfo = Contacts.query.all()

    return jsonify({"success": "you have successfully logged in"})

#this is the method that is going to update htier account information
@app.route("/update_account/<int:user_id>", methods=["POST"])
def update_account(user_id):
    user = Contacts.query.get(user_id)

    if not user:
        return jsonify({"error": "user not found"})

    data = request.json
    user.username = data.get("username", user.username)
    user.password = data.get("password", user.password)

    db.session.commit()

    return jsonify({"message": "your information has been updated"})

#this ithe route that is going to create a new account
@app.route('/create_account', methods=["POST"])
def create_user():
    username = request.json.get("username")
    password = request.json.get("password")

    if not username or not password:
        return jsonify({"error": "make sure to incude a first and last name"})

    new_account = Contacts(username=username, password=password)

    try: 
        db.session.add(new_account)
        db.session.commit()
    except Exception as e:
        return jsonify({"error": "something has gone wrong" + str(e)}), 400


    return jsonify({"message": "your account has been created"}), 201

#this is the route that is going to delete the user's account
@app.route("/delete_account/<int: user_id>", methods=["DELETE"])
def delete_account(user_id):
    user = Contacts.query.get(user_id)

    if not user:
        return jsonify("error": "User is not found"), 404

    db.session.delete(user)
    db.session.commit()

    return jsonify({"message": "the user has been deleted"}), 200

#if creates the databases and runs the backend app
if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)

#create an account 