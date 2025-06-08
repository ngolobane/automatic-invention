from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from main import db, User
import jwt
import datetime

auth_bp = Blueprint('auth', _name_)

# Registration
@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    
    if User.query.filter_by(username=data['username']).first():
        return jsonify({"error": "Username exists"}), 409
        
    hashed_pw = generate_password_hash(data['password'])
    new_user = User(
        username=data['username'],
        password_hash=hashed_pw,
        email=data.get('email')
    )
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify({"message": "User created"}), 201

# Login (JWT Token)
@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data['username']).first()
    
    if not user or not check_password_ha
