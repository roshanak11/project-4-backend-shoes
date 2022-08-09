from app import ma
from models.category import CategoryModel
# from marshmallow import fields

class CategorySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = CategoryModel
        load_instance = True

# DELETE
    # reviews = fields.Nested("ReviewSchema", many=True)
    # # ! Add clothes
    # clothes = fields.Nested("ClothingSchema", many=True)
