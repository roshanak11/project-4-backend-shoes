# from distuils.errors import CompileError
from models.shoe import ShoeModel
from models.review import ReviewModel
from models.category import CategoryModel
from models.shoe_category import ShoeCategoryModel



shoes_list = [
    CategoryModel(name="flat"),
    CategoryModel(name="heel"),
    CategoryModel(name="sandal"),
    CategoryModel(name="boot")
]

# ! Specifying the required column, the user_id, and it must exist because we seed users before everything else.
categories_list = [
    ShoeModel(name="pink heels", image="https://res.cloudinary.com/dgicm5dgb/image/upload/v1660241098/project-4-shoes/pink-heels_yvz4eb.jpg", description="pink heels", price=80, in_stock=True, user_id=1),
    ShoeModel(name="pink crocs", image="https://res.cloudinary.com/dgicm5dgb/image/upload/v1660751842/project-4-shoes/pink-crocs-sandal_u5k3a9.jpg", description="pink crocs", price=100, in_stock=True, user_id=1),
    ShoeModel(name="black high heel boots", image="https://res.cloudinary.com/dgicm5dgb/image/upload/v1660241345/project-4-shoes/black-high-heel-boots_uriaol.jpg", description="black high heel boots", price=120, in_stock=True, user_id=1),
    ShoeModel(name="black booties", image="https://res.cloudinary.com/dgicm5dgb/image/upload/v1660241348/project-4-shoes/black-booties_wjbaoj.jpg", description="black booties", price=90, in_stock=False, user_id=1)
]

# ! We now create this shoes_categories_list, which is responsible for creating the
# ! association, along with the quantity.
shoes_categories_list = [
    ShoeCategoryModel(shoe_id=1, category_id=2), #pink heels
    ShoeCategoryModel(shoe_id=1, category_id=3), #pink heels
    ShoeCategoryModel(shoe_id=2, category_id=1), #pink sandal
    ShoeCategoryModel(shoe_id=2, category_id=3), #pink sandal
    ShoeCategoryModel(shoe_id=3, category_id=2), #black high heel boots
    ShoeCategoryModel(shoe_id=3, category_id=4), #black high heel boots
    ShoeCategoryModel(shoe_id=4, category_id=1), #black booties
    ShoeCategoryModel(shoe_id=4, category_id=4) #black booties
]


# ! Specify the user_id on the ReviewModel
reviews_list = [
  ReviewModel(content="This is a great review", shoe_id=1, user_id=1)
]