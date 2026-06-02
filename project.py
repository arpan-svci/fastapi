from fastapi import FastAPI, Depends
from database import get_db, engine
from sqlalchemy.orm import Session
import model
from pydantic import BaseModel
from datetime import date
from typing import Optional

app = FastAPI()

class Book(BaseModel):
    id : Optional[int] = None 
    title : str
    author : str
    publish_date : date

@app.post("/book")
def create_book(book :Book, db: Session = Depends(get_db)):
    new_book = model.Book(id = book.id, title = book.title, author = book.author, publish_date = book.publish_date)
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book

@app.get("/books")
def get_book(db: Session = Depends(get_db)):
    books = db.query(model.Book).all()
    return books
