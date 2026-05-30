from pydantic import BaseModel

class UserDetails(BaseModel):
    name : str
    age : int

class Student(BaseModel):
    name: str
    age: int
    roll: int

class StudentResponse(BaseModel):
    name: str
    age: int