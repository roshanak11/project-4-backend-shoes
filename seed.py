
# ! Difference: our seed file knows about flask and SQLAlchemy
from app import app, db
from models.shoe_data import shoes_list, reviews_list, categories_list, shoes_categories_list
from models.user_data import user_list

# ! This basically ensures app and sb are ready for use and it provides
# ! 'scope' where I can access the app/db.
with app.app_context():
  # ! Try/catch in python is try/except
  try:
    print('Recreating database')
    db.drop_all() # ! Removing everything from the DB
    db.create_all() # ! This will create the TABLES in the database.

    print("seeding our database..")
    # ! Seed my users
    db.session.add_all(user_list)
    db.session.commit()

    db.session.add_all(shoes_list) # ! Add a list of things to DB
    db.session.commit() # ! Add, commit. Like git.
    
    db.session.add_all(categories_list)
    db.session.commit()

    db.session.add_all(shoes_categories_list)
    db.session.commit()

    # ! This has to come after making shoes. Because you need shoes to comment on.
    db.session.add_all(reviews_list)
    db.session.commit()
  
    print("bye")
  except Exception as e:
    print(e)