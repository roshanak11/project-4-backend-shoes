from app import db
# ! Importing base model, to use
from models.base import BaseModel
from models.shoe_category import ShoeCategoryModel
# ! Need to import CategoryModel here, for like 18 to create the relationship.
from models.category import CategoryModel
from models.review import ReviewModel
from models.user import UserModel

# ! ShoeModel EXTENDS BaseModel
# ! It ALSO extends db.Model
# ! Extending db.Model lets FSQLAlchemy
# ! 'know' about or model, so it can use it.
class ShoeModel(db.Model, BaseModel):

  # ! This will be used DIRECTLY to make a 
  # ! TABLE in Postgresql
    __tablename__ = "shoes"

    # ! Specific columns for our Shoe Table.
    name = db.Column(db.Text, nullable=False, unique=True)
    image = db.Column(db.Text, nullable=False, unique=True)
    description = db.Column(db.Text, nullable=False, unique=True)
    in_stock = db.Column(db.Boolean, nullable=False)
    price = db.Column(db.Integer, nullable=False)

    # ! Add a foreign key column to shoe. with user_id
    user_id = db.Column(db.Integer, db.ForeignKey("users.id", ondelete='CASCADE'), nullable=False)

   #DELETE # ! Letting flask-sqlalchemy know about my new table for category_shoe
   #DELETE # ! This is similar to relationship for reviews, but we tell
   #DELETE # ! it about the JOIN TABLE.
    # ! use the ShoeCategoryModel
    categories = db.relationship('ShoeCategoryModel', back_populates="shoe")

    # ! Moved the relationship to our main data class/parent (shoe)
    # # ! This line is for serialization. Tells our comment about our shoe model. 
    # # ! Associates 2 models together
    # # ! It won't make a new column, but instead, specifies a relationship between
    # # ! 2 models
    # # ? backref should be the table name of this current table.
    reviews = db.relationship("ReviewModel", backref="reviews", cascade="all, delete")
    # ! Add a user relationship to shoes
    # ! Make up a new backref for comment users, it can't be users because that backref exists already elsewhere
    user = db.relationship('UserModel', backref='users')

    