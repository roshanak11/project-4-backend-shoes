from datetime import datetime, timedelta
# ! Import jwt library (this is pyjwt)
import jwt
# ! Imported hybrid property
from sqlalchemy.ext.hybrid import hybrid_property
from app import db, bcrypt
from models.base import BaseModel
# ! Import my secret
from config.environment import secret



class UserModel(db.Model, BaseModel):

    __tablename__ = "users"

    username = db.Column(db.Text, nullable=False, unique=True)
    email = db.Column(db.Text, nullable=False, unique=True)

    # ! Password field h.
    password_hash = db.Column(db.Text, nullable=True)

<<<<<<< HEAD
    # ! We want to set a password field that doesn't get saved to the db, because we don't want to save original password
    # ! This will ensure you can provide a password field to this model when you try to create a User.
=======
    # ! I want to set a password field that doesn't get saved to the db, because I don't want to save original password
    # ! This will ensure I can provide a password field to this model when I try to create a User.
>>>>>>> 82102a472c85204303de9e5c693f612980459e39
    # ! This password will not be saved to db
    @hybrid_property
    def password(self):
        pass

    # ! I then use this password function as a decorator. It'll get called by Flask SQLAlchemy when the model gets created, BEFORE saving to the DB.
    @password.setter
    def password(self, password_plaintext):
<<<<<<< HEAD
        # ! Write our code to hash the password. It will give us back an encoded pw
=======
        # ! Write my code to hash the password. It will give me back an encoded password
>>>>>>> 82102a472c85204303de9e5c693f612980459e39
        encoded_pw = bcrypt.generate_password_hash(password_plaintext)
        # ! The decoded password that I actually want to store.
        self.password_hash = encoded_pw.decode('utf-8')

    # ! Use bcrypt to validate my password
    def validate_password(self, plaintext_password):
        return bcrypt.check_password_hash(self.password_hash, plaintext_password)

    def generate_token(self):
        # ! Create a token for this user.
        
        # ! Need a payload for the token
        payload = {
            # ! This will expire 3 days from now.
            "exp": datetime.utcnow() + timedelta(days=3),
            # ! The token was created (issued at):
            "iat": datetime.utcnow(),
            # ! Put the user id on the token to identify the user
            "sub": self.id
        }

        # ! Create the token itself/
        token = jwt.encode(
            payload, # ! provide the payload
            secret, # ! provide a secret
            algorithm="HS256"
        )

        print (token, type(token))

        return token