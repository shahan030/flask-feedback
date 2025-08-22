from flask import request, jsonify
from models.user import User
from database import db
import hashlib
from flask_jwt_extended import create_access_token

def signUp():
    data = request.get_json()
    username = data.get("username")
    email = data.get("email")
    password = data.get("password")

    if User.query.filter_by(email=email).first():
        return jsonify({"message": "Email already exists"}), 406

  
   
    new_user = User(username=username, email=email, password=password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User registered successfully"}), 200


def signIn():
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return jsonify({"message": "Email and password required"}), 400

  
    password_hash = hashlib.sha256(password.encode()).hexdigest()

   
    print("LOGGING IN:")
    print("Email entered:", email)
    print("Password entered:", password)
    print("Hash being searched:", password_hash)

 
    user = User.query.filter_by(email=email, password=password_hash).first()
    
    if not user:
        print(" No matching user found!")
        return jsonify({"message": "Invalid email or password"}), 401

    print(" User found! Logging in.")


    token = create_access_token(identity=user.id)

    return jsonify({
        "message": "Login successful",
        "token": token,
        "user": {
            "id": user.id,
            "username": user.username,
            "email": user.email
        }
    }), 200
