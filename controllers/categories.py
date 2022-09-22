

from http import HTTPStatus
from flask import Blueprint, request
from models.category import CategoryModel
from marshmallow.exceptions import ValidationError
from serializers.category import CategorySchema

category_schema = CategorySchema()

router = Blueprint("categories", __name__)

@router.route('/categories', methods=["POST"])
def create_category():
    category_dictionary = request.json

    try:
        category = category_schema.load(category_dictionary)
    except ValidationError as e:
        return {"errors": e.messages, "messages": "Something went wrong"}
    
    category.save()

    return category_schema.jsonify(category)



@router.route('/categories/<int:category_id>', methods=["DELETE"])
def remove_category(category_id):
    category = CategoryModel.query.get(category_id)

    if not category:
      return {"message": "Category not found"}, HTTPStatus.NOT_FOUND

    category.remove()

    return '', HTTPStatus.NO_CONTENT

    