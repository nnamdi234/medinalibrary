from db import books_collection
from models.book import Book
from fastapi import APIRouter

router = APIRouter(prefix="/books", tags = ['books'])

@router.post("/", response_model=Book)
def add_book(book: Book):
    book_dict = book.model_dump(exclude=["id"])
    result = books_collection.insert_one(book_dict)
    book_dict["_id"] = str(result.inserted_id)
    return Book(**book_dict)


@router.get("/", response_model=list[Book])
def get_books():
    books = list(books_collection.find())

    for book in books:
        book["_id"] = str(book["_id"])

    return [Book(**book) for book in books]