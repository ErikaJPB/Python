from fastapi import APIRouter
from config.db import conn
from models.user import users
from schemas.user import User

from cryptography.fernet import Fernet

key = Fernet.generate_key()
f = Fernet(key)

user = APIRouter()


@user.get("/users")
def get_users():
    return conn.execute(users.select()).fetchall()

@user.post("/users")
def create_user(user: User):
   new_user = {"name": user.name,"email": user.email}
   new_user["password"] = f.encrypt(user.password.encode("utf-8"))
   result = conn.execute(users.insert().values(**new_user))
   conn.commit()
   return {"id": result.lastrowid}
