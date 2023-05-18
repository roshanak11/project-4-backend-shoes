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

# ! Specifying the required column, the user_id, and it must exist because I seed users before everything else.
categories_list = [
    ShoeModel(name="stacy", image="https://res.cloudinary.com/dgicm5dgb/image/upload/v1660241098/project-4-shoes/pink-heels_yvz4eb.jpg", description="pink heels", price=80, in_stock=True, user_id=1),
    ShoeModel(name="mandy", image="https://res.cloudinary.com/dgicm5dgb/image/upload/v1660751842/project-4-shoes/pink-crocs-sandal_u5k3a9.jpg", description="pink crocs", price=100, in_stock=True, user_id=1),
    ShoeModel(name="sarah", image="https://res.cloudinary.com/dgicm5dgb/image/upload/v1660241345/project-4-shoes/black-high-heel-boots_uriaol.jpg", description="black high heel boots", price=120, in_stock=True, user_id=1),
    ShoeModel(name="jenny", image="https://res.cloudinary.com/dgicm5dgb/image/upload/v1660241348/project-4-shoes/black-booties_wjbaoj.jpg", description="black booties", price=90, in_stock=False, user_id=1),
    ShoeModel(name="tracy", image="https://res.cloudinary.com/dgicm5dgb/image/upload/v1661379388/project-4-shoes/greenheels_fcsxpm.webp", description="green heels", price=75, in_stock=True, user_id=1),
    ShoeModel(name="sandy", image="https://res.cloudinary.com/dgicm5dgb/image/upload/v1661379464/project-4-shoes/tanhighheelboots_f5wsog.webp", description="tan high heel boots", price=110, in_stock=True, user_id=1),
    ShoeModel(name="freya", image="https://res.cloudinary.com/dgicm5dgb/image/upload/v1661379941/project-4-shoes/whitehighheelboots_mlqm9a.jpg", description="white high heel cowboy boots", price=100, in_stock=True, user_id=1),
    ShoeModel(name="caroline", image="https://res.cloudinary.com/dgicm5dgb/image/upload/v1661379946/project-4-shoes/whitebooties_y1fbaf.jpg", description="white booties", price=95, in_stock=False, user_id=1),
    ShoeModel(name="julia", image="https://res.cloudinary.com/dgicm5dgb/image/upload/v1661380217/project-4-shoes/redheels_uzig7f.jpg", description="red heels", price=85, in_stock=True, user_id=1),
    ShoeModel(name="mary", image="https://res.cloudinary.com/dgicm5dgb/image/upload/v1661380223/project-4-shoes/yellowsandal_ivtgao.webp", description="yellow sandal", price=60, in_stock=True, user_id=1),
    ShoeModel(name="stefani", image="https://res.cloudinary.com/dgicm5dgb/image/upload/v1661380228/project-4-shoes/magentaheels_xnmhyq.webp", description="magenta heels", price=80, in_stock=True, user_id=1),
    ShoeModel(name="margot", image="https://res.cloudinary.com/dgicm5dgb/image/upload/v1661380643/project-4-shoes/whitehighheelnregularboots_jxmvb4.jpg", description="white high heel boots", price=105, in_stock=False, user_id=1),
    ShoeModel(name="christina", image="https://res.cloudinary.com/dgicm5dgb/image/upload/v1661380548/project-4-shoes/whiteheels_mdpbfa.webp", description="white heels", price=75, in_stock=True, user_id=1),
    ShoeModel(name="kasey", image="https://res.cloudinary.com/dgicm5dgb/image/upload/v1661380955/project-4-shoes/blueheels_l7rahe.webp", description="blue heels", price=95, in_stock=True, user_id=1),
    ShoeModel(name="sam", image="https://res.cloudinary.com/dgicm5dgb/image/upload/v1661381205/project-4-shoes/whitesandal_ucdvso.jpg", description="white sandal", price=65, in_stock=True, user_id=1),
    ShoeModel(name="delaney", image="https://res.cloudinary.com/dgicm5dgb/image/upload/v1661381200/project-4-shoes/tansandal_lqsnb0.jpg", description="tan sandal", price=70, in_stock=True, user_id=1),
    ShoeModel(name="jane", image="https://res.cloudinary.com/dgicm5dgb/image/upload/v1661381195/project-4-shoes/blacksandal_ehtjtq.jpg", description="black sandal", price=80, in_stock=True, user_id=1),
    ShoeModel(name="cassie", image="https://res.cloudinary.com/dgicm5dgb/image/upload/v1661381492/project-4-shoes/tanheels_qinlo3.jpg", description="tan heels", price=100, in_stock=True, user_id=1)
]

<<<<<<< HEAD
# ! We now create this shoes_categories_list, which is responsible for creating the
=======
# ! I now create this shoes_categories_list, which is responsible for creating the
>>>>>>> 82102a472c85204303de9e5c693f612980459e39
# ! association.
shoes_categories_list = [
    ShoeCategoryModel(shoe_id=1, category_id=2), #pink heels #stacy
    ShoeCategoryModel(shoe_id=1, category_id=3), #pink heels #stacy
    ShoeCategoryModel(shoe_id=2, category_id=1), #pink crocs #mandy
    ShoeCategoryModel(shoe_id=2, category_id=3), #pink crocs #mandy
    ShoeCategoryModel(shoe_id=3, category_id=2), #black high heel boots #sarah
    ShoeCategoryModel(shoe_id=3, category_id=4), #black high heel boots #sarah
    ShoeCategoryModel(shoe_id=4, category_id=1), #black booties #jenny
    ShoeCategoryModel(shoe_id=4, category_id=4), #black booties #jenny
    ShoeCategoryModel(shoe_id=5, category_id=2), #green heels #tracy
    ShoeCategoryModel(shoe_id=5, category_id=3), #green heels #tracy
    ShoeCategoryModel(shoe_id=6, category_id=2), #tan high heel boots #sandy
    ShoeCategoryModel(shoe_id=6, category_id=4), #tan high heel boots #sandy
    ShoeCategoryModel(shoe_id=7, category_id=2), #white high heel cowboy boots #freya
    ShoeCategoryModel(shoe_id=7, category_id=4), #white high heel cowboy boots #freya
    ShoeCategoryModel(shoe_id=8, category_id=1), #white booties #caroline
    ShoeCategoryModel(shoe_id=8, category_id=4), #white booties #caroline
    ShoeCategoryModel(shoe_id=9, category_id=2), #red heels #julia
    ShoeCategoryModel(shoe_id=9, category_id=3), #red heels #julia
    ShoeCategoryModel(shoe_id=10, category_id=1), #yellow sandal #mary
    ShoeCategoryModel(shoe_id=10, category_id=3), #yellow sandal #mary
    ShoeCategoryModel(shoe_id=11, category_id=2), #red heels #julia
    ShoeCategoryModel(shoe_id=11, category_id=3), #red heels #julia
    ShoeCategoryModel(shoe_id=12, category_id=2), #white high heel boots #margot
    ShoeCategoryModel(shoe_id=12, category_id=4), #white high heel boots #margot
    ShoeCategoryModel(shoe_id=13, category_id=2), #white heels #christina
    ShoeCategoryModel(shoe_id=13, category_id=3), #white heels #christina
    ShoeCategoryModel(shoe_id=14, category_id=2), #blue heels #kasey
    ShoeCategoryModel(shoe_id=14, category_id=3), #blue heels #kasey
    ShoeCategoryModel(shoe_id=15, category_id=1), #white sandal #sam
    ShoeCategoryModel(shoe_id=15, category_id=3), #white sandal #sam
    ShoeCategoryModel(shoe_id=16, category_id=1), #tan sandal #delaney
    ShoeCategoryModel(shoe_id=16, category_id=3), #tan sandal #delaney
    ShoeCategoryModel(shoe_id=17, category_id=1), #black sandal #jane
    ShoeCategoryModel(shoe_id=17, category_id=3), #black sandal #jane
    ShoeCategoryModel(shoe_id=18, category_id=2), #tan heels #cassie
    ShoeCategoryModel(shoe_id=18, category_id=3) #tan heels #cassie
]


# ! Here I specify the user_id on the ReviewModel
reviews_list = [
  ReviewModel(content="This is a great review", shoe_id=1, user_id=1)
]