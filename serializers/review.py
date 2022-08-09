
from app import ma
from models.review import ReviewModel
# ! Import fields
from marshmallow import fields


class ReviewSchema(ma.SQLAlchemyAutoSchema):

  class Meta:
    model = ReviewModel
    load_instance = True

  # ! Here is my single user
  user = fields.Nested("UserSchema", many=False)
  