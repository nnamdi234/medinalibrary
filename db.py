import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()


DATABASE_URL = os.getenv("DATABASE_URL")

database = MongoClient(DATABASE_URL)

db = database.get_default_database()
books_collection = db["books"]
user_collection = db["users"]


def ping():
    try:
        database.admin.command('ping')
        print("connected to the database successfully")
    except:
        print("could not connect to the database")