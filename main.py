#python
from typing import optional

#pydantic
from pydantic import BaseModel

#FastAPI
from fastapi import FastAPI
from fastapi import Body, Query

app = FastAPI()

#Models

class Location(BaseModel):
    city: str
    state: str
    country: str

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

#validations : query parameters

@app.get("/person/detail")
def show_person(
    name: Optional[str] = Query(
    None,
    min_length=1,
    max_length=50,
    title="Person name", #este seria el titulo de nuestra documentacion interactiva
    description="this is the persons name. between 1 and 50 characters" #esta es la desc de nuestra docu interactiva
    ),
    age: str = Query(
    ...,
    title="Person age",
    description="this is the person age. its requered"
    )
):
    return {name: age}

#validations path paramethers

@app.get("/person/detail/{person_id}")
def show_person(
    person_id: int = Path(..., gt=0)
):
    return {person_id "it exist!"}

#validations:request body

@app.put("/person/{person_id}")
def update_person(
    person_id: int = path(
    ...,
    title="Person ID",
    description="THis is the person ID",
    gt=0
    ),
    person: Person = Body(...),
    Location: Location = Body(...)
):
    results = person.dick()#es difisil retornar 2 valores, por eso lo convertimos a diccionario
    results .update(location.dict())
    return results


