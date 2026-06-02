from database import Base
from sqlalchemy import Column, Integer, String, Date

class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255))
    author = Column(String(255))
    publish_date = Column(Date)