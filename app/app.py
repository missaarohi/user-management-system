from flask import Flask
from flask_cors import CORS

from dotenv import load_dotenv
import os

from app.config import init_db
from app.routes import routes


load_dotenv()

app = Flask(__name__)
CORS(app)

app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

init_db(app)
app.register_blueprint(routes)

@app.route("/")
def home():
    return {"message": "Backend running successfully"}

if __name__ == "__main__":
       app.run(host="0.0.0.0", port=int(os.getenv("PORT", 5000)))

