from fastapi import FastAPI
from typing import Optional
from models import *


app = FastAPI()

@app.get("/")
def health():
    return {"message":"Hello World"}

@app.get("/greet")
def greet():
    return {"message":"Hello Arpan"}

@app.get("/{id}")
def printId(id: int):
    return {"message": id}

@app.get("/name/{name}")
def printName(name: str):
    return {"message": f"hello {name}"}

@app.get("/details")
def printDetails(id :int, name :str):
    return {"Id":id,"Name":name}

@app.get("/details/{name}")
def printLoop(name: str, number: int):
    message = []
    for i in range(number):
        message.append(f"Hello {name}")
    return {"message":message}

@app.get("/optional")
def OptionalPrint(name : Optional[str] = "User" , age : Optional[int] = 20):
    return {"message":f"Hello {name}, your age is {age}"}

@app.post("/userDetails")
def userDetails(user: UserDetails):
    return {"Details": user}

@app.get("/details/{name:str}/{age:int}")
def getDetails(name :str,age :int):
    return {"message":{"name":name,"age":age}}

@app.post("/createStudent",response_model=StudentResponse)
def createStudent(student: Student):
    return {
        "name":student.name,
        "age":student.age,
        "roll":student.roll
    }