from fastapi import FastAPI, status
from pydantic import BaseModel
from fastapi.exceptions import HTTPException

books = [
    {
        'id':1,
        'title': 'The Alchemist',
        'author': 'Paulo Coelho',
        'publishDate': '1988-01-01'
    },
    {
        'id':2,
        'title': 'The Power of Now',
        'author': 'Eckhart Tolle',
        'publishDate': '1997-01-01'
    },
    {
        'id':3,
        'title': 'The 7 Habits of Highly Effective People',
        'author': 'Stephen R. Covey',
        'publishDate': '1989-01-01'
    },
    {
        'id':4,
        'title': 'Atomic Habits',
        'author': 'James Clear',
        'publishDate': '2018-01-01'
    }
]

def findBookIndex(id: int):
    for index, book in enumerate(books):
        if book['id'] == id:
            return index
    return None

class Book(BaseModel):
    id: int
    title: str
    author: str
    publishDate: str

app = FastAPI()

@app.get('/books')
def getBooks():
    return {"books":books}

@app.post('/book')
def addBook(book :Book):
    newBook = book.model_dump()
    books.append(newBook)
    return {"message":"success"}

@app.put('/book/{id}')
def updateBook(id: int, book: Book):
    index = findBookIndex(id)
    if index is not None:
        books[index] = book.model_dump()
        return {"message":"success"}
    raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"Book with id {id} not found")

@app.delete('/book/{id}')
def deleteBook(id: int):
    index = findBookIndex(id)
    if index is not None:
        books.pop(index)
        return {"message":"success"}
    raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail=f"Book with id {id} not found")