
from app import db
from models.base import BaseModel

class CategoryModel(db.Model, BaseModel):

      __tablename__ = 'categories'

      name = db.Column(db.Text, nullable=False, unique=True)
    # ! Added this new relationship to the ShoeCategoryModel.
      shoes = db.relationship('ShoeCategoryModel', back_populates="category")