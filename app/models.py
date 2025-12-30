from datetime import datetime
from bson import ObjectId


def create_user(email, password, full_name,roll="user"):
    return {
        "email": email,
        "password": password,
        "full_name": full_name,
        "role": "user",
        "status": "active",
        "created_at": datetime.utcnow(),
        "updated_at": datetime.utcnow(),
        "last_login": None
    }


def user_response(user):
    return {
        "id": str(user["_id"]),
        "email": user["email"],
        "full_name": user["full_name"],
        "role": user["role"],
        "status": user["status"],
        "created_at": user["created_at"],
        "updated_at": user["updated_at"],
        "last_login": user.get("last_login")
    }
