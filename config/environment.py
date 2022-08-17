import os

db_URI = os.getenv('DATABASE_URL', 'postgresql://localhost:5432/shoes_db')
secret = os.getenv('SECRET', 'mysecret123')