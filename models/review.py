
# ! Creating a new comment model.
from app import db
from models.base import BaseModel

# ! 
class ReviewModel(db.Model, BaseModel):

    __tablename__ = "reviews"

    content = db.Column(db.Text, nullable=False)

    # ! ForeignKey tells you which column to point at
    # ! so that every comment points to a specific sgies
    # ! You give it the Primary Key of the shoes table. shoes.id
    shoe_id = db.Column(db.Integer, db.ForeignKey("shoes.id", ondelete='CASCADE'), nullable=False)


    # ! Moved the relationship to models/shoe.py
    # # ! This line is for serialization. Tells our comment about our shoe model
    # # ! Associates 2 models together
    # # ! It won't make a new column, but instead, specifies a relationship between
    # # ! 2 models
    # # ? backref should be the table name of this current table.
    # barbie = db.relationship("ShoeModel", backref="reviews")

    # ! Add a foreign key column to barbie. with user_id
    user_id = db.Column(db.Integer, db.ForeignKey("users.id", ondelete='CASCADE'), nullable=False)

    # ! Make up a new backref for comment users, it can't be
    # ! users because that backref exists elsewhere.
    user = db.relationship('UserModel', backref='review_users')