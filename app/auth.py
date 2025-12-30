import bcrypt
import jwt
import datetime
import os
from functools import wraps
from flask import request


def hash_password(password: str) -> bytes:
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode("utf-8"), salt)


def verify_password(password: str, hashed_password: bytes) -> bool:
    return bcrypt.checkpw(password.encode("utf-8"), hashed_password)


def generate_jwt(user_id):
    payload = {
        "user_id": str(user_id),
        "iat": datetime.datetime.utcnow(),
        "exp": datetime.datetime.utcnow()
        + datetime.timedelta(minutes=int(os.getenv("JWT_EXP_MINUTES", 60)))
    }

    token = jwt.encode(
        payload,
        os.getenv("JWT_SECRET"),
        algorithm="HS256"
    )
    return token

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth_header = request.headers.get("Authorization")

        if not auth_header:
            return {"error": "Authorization token missing"}, 401

        try:
            token = auth_header.split(" ")[1]
            payload = jwt.decode(
                token,
                os.getenv("JWT_SECRET"),
                algorithms=["HS256"]
            )
            request.user_id = payload["user_id"]
        except Exception:
            return {"error": "Invalid or expired token"}, 401

        return f(*args, **kwargs)

    return decorated
