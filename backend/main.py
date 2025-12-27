from flask improt request, jsonify
from config import app,db
from models import Contacts

@app.route('/', methods=["POST"])
def authUser():
    userInfo = Contact.query.all()
    
    return jsonify({"success": "you have successfully logged in"})


if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)

#create an account 