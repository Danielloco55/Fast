#python
from typing import Optional
from enum import Enum

#pydantic
from pydantic import BaseModel
from pydantic import Field

#FastAPI
from fastapi import FastAPI
from fastapi import status
from fastapi import Body, Query

app = FastAPI()

#Models

class HairColor(Enum):
    white = "White"
    brown = "Borwn"
    Black = "Black"
    Blonde = "Blonde"
    red = "red"

class Location(BaseModel):
    city: str
    state: str
    country: str


class PersonBase(BaseModel):
    first_name: str = Field(
        ...,
        min_length=1,
        max_length=50,
        example= "Daniel"
        )
    las_name: str = Field(
        ...,
        min_length=1,
        max_length=50
        example= "Gonzalez"
        )
    age: int = Field(
        ...,
        gt=0,
        le=115
        example=25
    )
    hair_color: optional[HairColor] = Field(default=None, example="black")
    is_married: optional[bool] = Field(default=None, example=False)
    
class Person(PersonBase):
    password: str = Field(..., min_length=8)

#class Config:
    #schema_extra = {
        #"example": {
        #"first_name": "Daniel"
        #"last_name": "Gonzalez Acosta",
        #"age": 21,
        #"hair_color": "blonde",
        #"is_married": False
        #}
    #}

class personOut(PersonBase):


@app.get(
        path="/",
        status_code=status.HTTP_200_0K
        )
def home():
    return {"Hello": "world"}
#request and response body


@app.post(
        path="/person/new",
        response_model=PersonOut
        status_code=status.HTTP_201_CREATED
        )  #path operation decorator
def create_person(person: Person = Body(...)): #path operation function
    return Person

#validations : query parameters

@app.get(
        path="/person/detail",
        status_code=status.HTTP_200_OK
        )
def show_person(
    name: Optional[str] = Query(
    None,
    min_length=1,
    max_length=50,
    title="Person name", #este seria el titulo de nuestra documentacion interactiva
    description="this is the persons name. between 1 and 50 characters" #esta es la desc de nuestra docu interactiva
    , example="Daniel"),
    age: str = Query(
    ...,
    title="Person age",
    description="this is the person age. its requered",
    example="27"
    )
):
    return {name: age}

#validations path paramethers

@app.get("/person/detail/{person_id}")
def show_person(
    person_id: int = Path(
    ...,
    gt=0,
    example="123")
):
    return {person_id "it exist!"}

#validations:request body

@app.put("/person/{person_id}")
def update_person(
    person_id: int = path(
    ...,
    title="Person ID",
    description="THis is the person ID",
    gt=0,
    example=123
    ),
    person: Person = Body(...),
    Location: Location = Body(...)
):
    results = person.dick()#es difisil retornar 2 valores, por eso lo convertimos a diccionario
    results .update(location.dict())
    return results


