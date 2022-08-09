from http import HTTPStatus
# ! Adding this new users controller
from flask import Blueprint, request
from models.user import UserModel
from serializers.user import UserSchema
from marshmallow.exceptions import ValidationError

# TODO Add serializer later
user_schema = UserSchema()

router = Blueprint("users", __name__)

@router.route('/register', methods=["POST"])
def register():
    try:
        user_dictionary = request.json
        user = user_schema.load(user_dictionary)
        user.save()
        return user_schema.jsonify(user)
    # ! Specific error
    except ValidationError as e:
        return {"errors": e.messages, "messages": "Something went wrong validating"}
    # ! General error
    except Exception as e:
        print(e)
        return { "messages": "Something went wrong" }


@router.route('/login', methods=["POST"])
def login():
    try:
        # ! Get the credentials for logging in.
        credentials_dictionary = request.json
        # ! First, grab the user from postgresql by their email
        user = UserModel.query.filter_by(email=credentials_dictionary["email"]).first()
        # ! If there's no user, return
        if not user:    
            return {"message": "No user found for this email"}
        # ! Check the password matches the hashed one stored.
        if not user.validate_password(credentials_dictionary["password"]):
            return {"message": "You are not authorized"}, HTTPStatus.UNAUTHORIZED
        # ! Make a token
        token = user.generate_token()
        # ! Send it back
        return {"token": token, "message": "Welcome back!"}
    
    except Exception as e:
        return { "messages": "Something went wrong"}