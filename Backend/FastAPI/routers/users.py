from fastapi import APIRouter, HTTPException
from pydantic import BaseModel


router = APIRouter(prefix="/users", tags=["users"], responses={404: {"description": "Not found"}})


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


# @router.get("/usersjson")
# async def usersjson():
#     return [{"name" : 'Erika', "lastname" : "Pineda", "age" : 30 },
#             {"name" : 'Juan', "lastname" : "Perez", "age" : 26 }, 
#             {"name" : 'Diego', "lastname" : "Alvarez", "age" : 34 },
#             {"name" : 'Andrea', "lastname" : "Ortiz", "age" : 23 },
#             {"name" : 'Fabian', "lastname" : "Jimenez", "age" : 32 }]

# Get users
@router.get("/", response_model=list[User])
async def get_users():
    return users_list


# Get user by id - Path
@router.get("/{id}", response_model=User)
async def get_user_by_id(id: int):
    user = search_user(id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

   

# Get user by query
@router.get("/user/", response_model=User)
async def get_user_by_query(id: int) :
    user = search_user(id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

# Create user
@router.post("/user/", response_model=User, status_code=201)
async def create_user(user: User):
    if search_user(user.id):
        raise HTTPException(status_code=400, detail="User already exists")
    users_list.append(user)
    return user

# Update user
@router.put("/user/", response_model=User)
async def update_user(user: User):
    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index] = user
            return user
    raise HTTPException(status_code=404, detail="User not found")
    
  
# Delete user
@router.delete("/user/{id}", response_model=dict)
async def delete_user(id: int):
    for index, saved_user in enumerate(users_list):
        if saved_user.id == id:
            del users_list[index]
            return {"message": "User deleted successfully"}
    raise HTTPException(status_code=404, detail="User not found")
          
  
# Search user function
def search_user(id: int) -> User | None:
    for user in users_list:
        if user.id == id:
            return user
    return None