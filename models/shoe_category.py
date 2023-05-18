from app import db
from models.base import BaseModel


# ! I need this new class ShoeCategoryModel, called an Association Object
# ! I used the documentation here to guide me:
# ? https://docs.sqlalchemy.org/en/14/orm/basic_relationships.html#association-object
class ShoeCategoryModel(db.Model, BaseModel):

    __tablename__ = "shoes_categories"

    shoe_id = db.Column(db.Integer, db.ForeignKey("shoes.id"))
    category_id = db.Column(db.Integer, db.ForeignKey("categories.id"))

    shoe = db.relationship("ShoeModel", back_populates="categories")
    category = db.relationship("CategoryModel", back_populates="shoes")
