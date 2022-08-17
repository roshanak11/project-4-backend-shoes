# 1 import flask-sqlalchemy db
from app import db
from datetime import *

# ! Our first FLask SQLAlchemy model.
# ? - It is a class in python.
# ? - Flask SQLAlchemy will create tables based on these models.
# ? In other words, SQL is written for you.

# * A class that has all the COMMON fields
# * that EVERY model will use.
class BaseModel:

    # ! This is a static field. I don't need to make an object to set this value.
    # ! It's a way of specifying fields that don't change in value.
    id = db.Column(db.Integer, primary_key=True)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )

    # ! Add a method here to save my model to the database
    def save(self):
        db.session.add(self)
        db.session.commit()

    # ! Add a method to remove
    def remove(self):
        db.session.delete(self)
        db.session.commit()
