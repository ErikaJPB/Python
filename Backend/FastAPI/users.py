from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


# start the server : python -m uvicorn users:app --reload



# USER

class User(BaseModel):
    id: int
    name: str
    lastname: str
    age: int


users_list = [
    User(id=1, name="Erika", lastname="Pineda", age=30),
    User(id=2, name="Juan", lastname="Perez", age=26),
    User(id=3, name="Diego", lastname="Alvarez", age=34),
    User(id=4, name="Andrea", lastname="Ortiz", age=23),
    User(id=5, name="Fabian", lastname="Jimenez", age=32),
]


@app.get("/usersjson")
async def usersjson():
    return [{"name" : 'Erika', "lastname" : "Pineda", "age" : 30 },
            {"name" : 'Juan', "lastname" : "Perez", "age" : 26 }, 
            {"name" : 'Diego', "lastname" : "Alvarez", "age" : 34 },
            {"name" : 'Andrea', "lastname" : "Ortiz", "age" : 23 },
            {"name" : 'Fabian', "lastname" : "Jimenez", "age" : 32 }]


@app.get("/users")
async def users():
    return users_list

# Path
@app.get("/user/{id}")
async def user(id: int):
    return search_user(id)
   
# Query
@app.get("/user/")
async def user(id: int) :
    return search_user(id)

def search_user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error": "User not found" }
    

