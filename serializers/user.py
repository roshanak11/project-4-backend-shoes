from marshmallow import fields

# ! Creating a new serializer
from app import ma
from models.user import UserModel


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = UserModel
        load_instance = True
        # ! New capabilities of marshmallow! Must add comma for it to be a TUPPLE
        exclude = ("password_hash",)
        # ! ONLY INCLUDE THESE FIELDS IN DESERIALIZATION (.load method)
        load_only = ('email', 'password')

    # ! Tells the serializer to expect a password field
    # ! (in other words, because it's a column in User)
    password = fields.String(required=True) 