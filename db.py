import os
from dotenv import load_dotenv
from pymongo import MongoClient


load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

client = MongoClient(DATABASE_URL)

def ping():
    try:
        client.admin.command("ping")
        print("Connected to the database successfully")
    except Exception as e:
        print("Could not connect to the database")
        print(e)