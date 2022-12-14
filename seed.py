
# ! My seed file knows about flask and SQLAlchemy
from app import app, db
from models.shoe_data import shoes_list, reviews_list, categories_list, shoes_categories_list
from models.user_data import user_list

# ! This basically ensures app and database are ready for use and it provides
# ! 'scope' where I can access the app/database.
with app.app_context():
  # ! Try/catch in python is try/except
  try:
    print('Recreating database')
    db.drop_all() # ! Removing everything from the database
    db.create_all() # ! This will create the TABLES in the database.

    print("seeding our database..")
    # ! Seed my users
    db.session.add_all(user_list)
    db.session.commit()

    db.session.add_all(shoes_list) # ! Add a list of things to database
    db.session.commit() # ! Add, commit. Like git.
    
    db.session.add_all(categories_list)
    db.session.commit()

    db.session.add_all(shoes_categories_list)
    db.session.commit()

    # ! This has to come after making shoes. Because I need shoes to comment on.
    db.session.add_all(reviews_list)
    db.session.commit()
  
    print("bye")
  except Exception as e:
    print(e)