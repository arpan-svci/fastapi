from fastapi import FastAPI


app = FastAPI()

@app.get("/")
def health():
    return {"message":"Hello World"}

@app.get("/greet")
def greet():
    return {"message":"Hello Arpan"}
