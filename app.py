from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
# ! import Bcrypt.
from flask_bcrypt import Bcrypt
from flask_cors import CORS

from config.environment import db_URI

# ? Instantiate flask
# ? __name__ is going to be a different value depending on
# ? where you run flask from. If you run this directly,
# ? it will be '__main__'
app = Flask(__name__)
CORS(app)

app.config["SQLALCHEMY_DATABASE_URI"] = db_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

ma = Marshmallow(app)

# ! Instantiate Bcrypt class.
bcrypt = Bcrypt(app)

from controllers import shoes, categories, users

app.register_blueprint(shoes.router, url_prefix="/api")
app.register_blueprint(categories.router, url_prefix="/api")
app.register_blueprint(users.router, url_prefix="/api")