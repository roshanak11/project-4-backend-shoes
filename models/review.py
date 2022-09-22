
# ! Creating a new comment model.
from app import db
from models.base import BaseModel

class ReviewModel(db.Model, BaseModel):

    __tablename__ = "reviews"

    content = db.Column(db.Text, nullable=False)

    # ! ForeignKey tells me which column to point at
    # ! so that every comment points to a specific shoe
    # ! You give it the Primary Key of the shoes table: shoes.id
    shoe_id = db.Column(db.Integer, db.ForeignKey("shoes.id", ondelete='CASCADE'), nullable=False)

    # ! Add a foreign key column to shoe with users.id
    user_id = db.Column(db.Integer, db.ForeignKey("users.id", ondelete='CASCADE'), nullable=False)

    # ! Make up a new backref for comment users, it can't be
    # ! users because that backref exists elsewhere.
    user = db.relationship('UserModel', backref='review_users')