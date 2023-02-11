#python
from typing import optional

#pydantic
from pydantic import BaseModel

#FastAPI
from fastapi import FastAPI
from fastapi import Body

app = FastAPI()

#Models

class Person(BaseModel):
    first_name: str
    las_name: str
    age: int
    hair_color: optional[str] = None
    is_married: optional[bool] = None

@app.get("/")
def home():
    return {"Hello": "world"}

#request and response body

@app.post("/person/new")  #path operation decorator
def create_person(person: Person = Body(...)): #path operation function
    return Person
