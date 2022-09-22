from app import ma
from models.category import CategoryModel
# from marshmallow import fields

class CategorySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = CategoryModel
        load_instance = True

