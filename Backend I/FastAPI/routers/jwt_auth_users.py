from fastapi import APIRouter, Depends, status, HTTPException
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from datetime import datetime, timedelta

ALGORITHM = "HS256"
ACCESS_TOKEN_DURATION = 1
SECRET = "89fe13b8c21a546d22227b7c5630a3b6eb2c56282895d632caedac02f38c91f4090ccb96e90f26b0"

router = APIRouter(
    prefix="/jwtauth",
    tags=["jwtauth"],
    responses={status.HTTP_404_NOT_FOUND: {"description": "Not found"}}
)

oauth2 = OAuth2PasswordBearer(tokenUrl="/jwtauth/login")

crypt = CryptContext(schemes=["bcrypt"])

class User(BaseModel):
    username: str
    full_name: str
    email: str
    disabled: bool


class UserDB(User):
    password: str


users_db = {
    "johndoe": {
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "johndoe@example.com",
        "disabled": False,
        "password": "$2a$12$hkwv.8OReUjc6NdOxpKk4.fXkV.4E3fIJVFUO26mHii754rLk74dq"
    },
    "janedoe": {
        "username": "janedoe",
        "full_name": "Jane Doe",
        "email": "janedoe@example.com",
        "disabled": True,
        "password": "$2a$12$RNPx6R/BfKL92vIQ3q3lMOQGDw0zqfeja5YVFij.x58u1rH/JTPBm"
    },
}

def search_user_db(username: str):
    if username in users_db:
        return UserDB(**users_db[username])
    return None


def search_user(username: str):
    if username in users_db:
        return User(**users_db[username])
    return None


async def authenticate_user(token : str = Depends(oauth2)):
   exception = HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Could not validate credentials",
                headers={"WWW-Authenticate": "Bearer"})
   try:
        username = jwt.decode(token, SECRET, algorithms=[ALGORITHM]).get("sub")
        if username is None:
            raise exception

   except JWTError: 
        raise exception
   
   return search_user(username)
   
           
    
async def current_user(user: User = Depends(authenticate_user)):
    if user.disabled:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail="Inactive User")
    
    return user
  


@router.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user_db = users_db.get(form.username)
    if not user_db:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid User"
        )

    user = search_user_db(form.username)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid User"
        )

    if not crypt.verify(form.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Incorrect Password"
        )

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_DURATION)
    access_token = jwt.encode(
        {"sub": user.username, "exp": datetime.utcnow() + access_token_expires},
        SECRET,
        algorithm=ALGORITHM
    )

    return {"access_token": access_token, "token_type": "bearer"}


@router.get("/users/me")
async def get_me(user: User = Depends(current_user)):
    return user