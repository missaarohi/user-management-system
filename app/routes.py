from flask import Blueprint, request
from app.config import mongo
from app.models import create_user, user_response
from app.auth import (
    hash_password,
    verify_password,
    generate_jwt,
    token_required
)
from datetime import datetime
from bson import ObjectId
import re

routes = Blueprint("routes", __name__)


def is_valid_email(email):
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(pattern, email)


@routes.route("/signup", methods=["POST"])
def signup():
    data = request.json

    if not data:
        return {"error": "Invalid request"}, 400

    email = data.get("email")
    password = data.get("password")
    full_name = data.get("full_name")

    if not email or not password or not full_name:
        return {"error": "All fields are required"}, 400

    if not is_valid_email(email):
        return {"error": "Invalid email format"}, 400

    if mongo.db.users.find_one({"email": email}):
        return {"error": "Email already registered"}, 409

    hashed_password = hash_password(password)

    user_data = create_user(email, hashed_password, full_name)
    result = mongo.db.users.insert_one(user_data)

    new_user = mongo.db.users.find_one({"_id": result.inserted_id})

    return {
        "message": "User registered successfully",
        "user": user_response(new_user)
    }, 201


@routes.route("/login", methods=["POST"])
def login():
    data = request.json

    if not data:
        return {"error": "Invalid request"}, 400

    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return {"error": "Email and password required"}, 400

    user = mongo.db.users.find_one({"email": email})

    if not user or not verify_password(password, user["password"]):
        return {"error": "Invalid credentials"}, 401

    mongo.db.users.update_one(
        {"_id": user["_id"]},
        {"$set": {"last_login": datetime.utcnow()}}
    )

    token = generate_jwt(user["_id"])

    return {
        "message": "Login successful",
        "token": token,
        "user": user_response(user)
    }, 200


@routes.route("/me", methods=["GET"])
@token_required
def get_me():
    user = mongo.db.users.find_one(
        {"_id": ObjectId(request.user_id)}
    )

    if not user:
        return {"error": "User not found"}, 404

    return {
        "user": user_response(user)
    }, 200


@routes.route("/admin/users", methods=["GET"])
@token_required
def get_all_users():
    user = mongo.db.users.find_one(
        {"_id": ObjectId(request.user_id)}
    )

    if not user or user["role"] != "admin":
        return {"error": "Access denied"}, 403

    users = mongo.db.users.find()
    return {
        "users": [user_response(u) for u in users]
    }, 200
