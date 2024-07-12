from fastapi import APIRouter, HTTPException, status
from db.models.user import User
from db.schemas.user import user_schema, users_schema
from db.client import db_client
from bson import ObjectId

router = APIRouter(
    prefix="/usersdb",
    tags=["usersdb"],
    responses={status.HTTP_404_NOT_FOUND: {"message": "Not found"}}
)

def search_user(field: str, key) -> User:
    user = db_client.users.find_one({field: key})
    if user:
        return User(**user_schema(user))
    else:
        return None

@router.get("/", response_model=list[User])
async def get_users():
    return users_schema(db_client.users.find())

# Path
@router.get("/{id}", response_model=User)  
async def get_user_by_id(id: str):
    return search_user("_id", ObjectId(id))

# Query
@router.get("/", response_model=User) 
async def get_user_by_query(id: str):
    return search_user("_id", ObjectId(id))


@router.post("/", response_model=User, status_code=status.HTTP_201_CREATED)
async def create_user(user: User):
    if search_user("email", user.email) is not None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="User already exists")

    user_dict = dict(user)
    del user_dict["id"]

    id = db_client.users.insert_one(user_dict).inserted_id
    
    new_user = user_schema(db_client.users.find_one({"_id": id}))

    return User(**new_user)

@router.put("/", response_model=User)
async def update_user(user: User):

    user_dict = dict(user)
    del user_dict["id"]

    try:
        db_client.users.find_one_and_replace(
        {"_id": ObjectId(user.id)}, user_dict)

    except: 
        return {"error": "User not found"}

    
    return search_user("_id", ObjectId(user.id))



@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(id: str):
    result = db_client.users.find_one_and_delete({"_id": ObjectId(id)})

    if result is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
