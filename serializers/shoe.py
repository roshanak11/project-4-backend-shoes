from app import ma
from models.shoe import ShoeModel
# ! Import fields from marshmallow
from marshmallow import fields

# ! Care with the casing here.
# ! Extending the marshmallow serializer schema
# ? A schema says how to serialize:
# Python Model -> JSON
# Python Dictionary -> Python Model

# Python Model -> JSON
class ShoeSchema(ma.SQLAlchemyAutoSchema):
    # ! Nested inner class called Meta
    class Meta:
      # ! A property on this class, where I tell it about
      # ! my model. It has to be called model.
      model = ShoeModel
      # Python Dictionary -> Python Model
      # ! I need to tell Marshmallow to give me back a MODEL when I deserialize, rather than a dictionary:
      load_instance = True

    # ! This will nest comments inside of shoe
    # ! First argument to Nested is the name of schema to nest..
    # ! Second argument is if there's a list many=True
    reviews = fields.Nested("ReviewSchema", many=True)

    categories = fields.Nested("CategorySchema", many=True)
    # ! Get my user for this shoe
    user = fields.Nested("UserSchema", many=False)