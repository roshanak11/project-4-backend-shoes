
from curses.ascii import HT
from http import HTTPStatus
# * Here is my controller for shoes (also the views).


# * Flask's router is called Blueprint
# ! Also importing request!!!
# ! import g
from flask import Blueprint, request, g
# ! Import Validation Error from Marshmallow
from marshmallow.exceptions import ValidationError
# ! Import the serializer
from serializers.shoe import ShoeSchema
from serializers.review import ReviewSchema
from models.shoe import ShoeModel
from models.review import ReviewModel
from models.category import CategoryModel
from serializers.shoe import ShoeSchema
from serializers.review import ReviewSchema
from serializers.category import CategorySchema

from middleware.secure_route import secure_route

# ! Instantiate the schema
shoe_schema = ShoeSchema()
review_schema = ReviewSchema()
category_schema = CategorySchema()

# * Instantiate my router (Blueprint is a class)
# ? This takes __name__, and a unique
# ? name to register e.g. "shoes"
router = Blueprint("shoes", __name__)



# * GET all Shoes
# ? Make a very basic route to talk to...
# * This @ syntac is a 'Decorator'. This decorator tells us
# * Which route our function belongs to (our path for this route).
@router.route("/shoes", methods=["GET"])
def get_shoes():
    # ! My shoes live in postgres.
    # ! Use SQLAlchemy to get shoes
    shoes = ShoeModel.query.all() # ! query is an object that lives on a model
    # ! query has methods like .all, to interact with the database

    # ! Serializing to shoes json using .jsonify.
    # ! many=True tells the serialiizer I am giving it a list of shoe models.
    return shoe_schema.jsonify(shoes, many=True), HTTPStatus.OK


# * GET single Shoe
# ? <TYPE:PARAM_NAME>
# ? TYPE is your type, e.g. int
# ? PARAM_NAME is your parameter
@router.route("/shoes/<int:shoe_id>")
# ! I'm passing the shoe_id as an argument.
def get_single_shoe(shoe_id):
    
    shoe = ShoeModel.query.get(shoe_id)
    
    # ! Empty dictionary -> Boolean gives me...False
    if not shoe:
      # ! Return a tuple with message not found and status code.
      return {"message": "Shoe not found" }, HTTPStatus.NOT_FOUND

    return shoe_schema.jsonify(shoe), HTTPStatus.OK



# * Post a Shoe!
@router.route("/shoes", methods=["POST"])
@secure_route
def create_shoe():
    shoe_dictionary = request.json

    print(shoe_dictionary, type(shoe_dictionary))

    # ! Turn this dictionary -> ShoeModel
    # ! This could cause Validation Error, so I'm try excepting.
    try:
      # ! .load will deserialize dictionary -> ShoeModel
      shoe = shoe_schema.load(shoe_dictionary)
    # ! Marshmallow provides validation error for me.
    except ValidationError as e:
      return { "errors": e.messages, "message": "Something went wrong" }

    print(shoe_dictionary, type(shoe))


    # ! Add the current user
    shoe.user_id = g.current_user.id
    # ! Save my shoe, using the methods I defined on BaseModel
    shoe.save()

    # jsonthing = shoe_schema.jsonify(shoe)
    # print(jsonthing, type(jsonthing))

    return shoe_schema.jsonify(shoe), HTTPStatus.CREATED


# ! PUT Shoe
@router.route("/shoes/<int:shoe_id>", methods=["PUT"])
@secure_route
def update_shoe(shoe_id):
    shoe_dictionary = request.json
    existing_shoe = ShoeModel.query.get(shoe_id)

    if not existing_shoe:
        return {"message": "Shoe not found"}, HTTPStatus.NOT_FOUND

    # ! Add this check whenever I want to make sure the shoe is the user's shoe that they're trying to update/delete
    if not g.current_user.id == existing_shoe.user_id:
        return{"message": "Not your Shoe!"}, HTTPStatus.UNAUTHORIZED

    try:
        shoe = shoe_schema.load(shoe_dictionary, instance=existing_shoe, partial=True)
    
    except ValidationError as e:
        return {"errors": e.messages, "messages": "Something went wrong"}

    shoe.save()

    return shoe_schema.jsonify(shoe), HTTPStatus.OK


# ! DELETE SHOE
@router.route("/shoes/<int:shoe_id>", methods=["DELETE"])
@secure_route
def remove_shoe(shoe_id):
    shoe = ShoeModel.query.get(shoe_id)

    if not shoe:
        return {"message:" "Shoe not found"}, HTTPStatus.NOT_FOUND

    shoe.remove()

    return '', HTTPStatus.NO_CONTENT






# ! POSTing a review
@router.route('/shoes/<int:shoe_id>/reviews', methods=['POST'])
@secure_route
def create_review(shoe_id):

    review_dictionary = request.json
  
    try:
        review = review_schema.load(review_dictionary)

    except ValidationError as e:
        return { "errors": e.messages, "message": "Something went wrong" }
    
    review.shoe_id = shoe_id
    # ! Get the current_user.id from our global object
    # ! g imported above
    review.user_id = g.current_user.id
    review.save()

    return review_schema.jsonify(review), HTTPStatus.CREATED




# ! PUTTing a review
@router.route("/shoes/<int:shoe_id>/reviews/<int:review_id>", methods=["PUT"])
@secure_route
def update_review(shoe_id, review_id):

    review_dictionary = request.json
    existing_review = ReviewModel.query.get(review_id)

    if not existing_review:
        return {"message": "Review not found"}, HTTPStatus.NOT_FOUND

    try:
        review = review_schema.load(
          review_dictionary, # ! All the fields I'm changing
          instance=existing_review, # ! Existing review I'm updating
          partial=True # ! This allows me to ONLY provide the fields you're changing
        )

    except ValidationError as e:
        return {"errors": e.messages, "messages": "Something went wrong"}

    review.save()

    shoe = ShoeModel.query.get(shoe_id)

    if not shoe:
        return {"message": "Shoe not found"}, HTTPStatus.NOT_FOUND

    return shoe_schema.jsonify(shoe), HTTPStatus.OK

# ! DELETING a review
@router.route("/shoes/<int:shoe_id>/reviews/<int:review_id>", methods=["DELETE"])
@secure_route
def remove_review(shoe_id, review_id):

    review = ReviewModel.query.get(review_id)

    if not review:
        return {"message": "Review not found"}, HTTPStatus.NOT_FOUND

    review.remove()

    shoe = ShoeModel.query.get(shoe_id)

    if not shoe:
        return {"message": "Shoe not found"}, HTTPStatus.NOT_FOUND

    return shoe_schema.jsonify(shoe), HTTPStatus.OK



# ! Here we are association (creating a relationship between)
# ! A Shoe and a Category.
@router.route("/shoes/<int:shoe_id>/categories/<int:category_id>", methods=["POST"])
@secure_route
def create_shoe_category(shoe_id, category_id):
    # ! This assumes both the category and the shoe exists.

    shoe = ShoeModel.query.get(shoe_id)

    category = CategoryModel.query.get(category_id)

    if not category or not shoe:
        return {"message": "item not found"}, HTTPStatus.NOT_FOUND

    # ! This is possible because of the relationship field in ShoeModel
    # ! Add the category to the shoe. This defines the relationship.
    shoe.categories.append(category)

    shoe.save()

    return shoe_schema.jsonify(shoe), HTTPStatus.OK