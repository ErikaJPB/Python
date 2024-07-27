from fastapi import APIRouter, HTTPException
from config.db import conn
from models.user import users
from schemas.user import User
from sqlalchemy.exc import SQLAlchemyError
from cryptography.fernet import Fernet

key = Fernet.generate_key()
f = Fernet(key)

user = APIRouter(prefix="/users", tags=["users"])


@user.get("/")
def get_users():
    try:
        result = conn.execute(users.select()).fetchall()
        return [dict(row._mapping) for row in result]
    except SQLAlchemyError as error:
        raise HTTPException(status_code=500, detail=str(error))


@user.post("/")
def create_user(user: User):
    new_user = {"name": user.name, "email": user.email}
    new_user["password"] = f.encrypt(user.password.encode("utf-8"))
    try:
        result = conn.execute(users.insert().values(**new_user))
        conn.commit()
        return {"message": "User created successfully", "user": new_user}
    except SQLAlchemyError as error:
        conn.rollback()
        raise HTTPException(status_code=500, detail=str(error))


@user.get("/{id}")
def get_user(id: str):
    try:
        result = conn.execute(users.select().where(users.c.id == id)).first()
        if result:
            user = dict(result._mapping)
            return user
        else:
            raise HTTPException(status_code=404, detail="User not found")
    except SQLAlchemyError as error:
        raise HTTPException(status_code=500, detail=str(error))


@user.put("/{id}")
def update_user(id: str, user: User):
    update_data = {"name": user.name, "email": user.email}
    if user.password:
        update_data["password"] = f.encrypt(user.password.encode("utf-8"))

    try:
        result = conn.execute(users.update().where(
            users.c.id == id).values(**update_data))
        conn.commit()
        if result.rowcount == 0:
            raise HTTPException(status_code=404, detail="User not found")
        updated_user = conn.execute(
            users.select().where(users.c.id == id)).fetchone()
        if updated_user:
            user_data = dict(updated_user._mapping)
            return {"message": "User updated successfully", "user": user_data}
        else:
            raise HTTPException(status_code=404, detail="User not found")
    except SQLAlchemyError as error:
        conn.rollback()
        raise HTTPException(status_code=500, detail=str(error))


@user.delete("/{id}")
def delete_user(id: str):
    try:
        result = conn.execute(users.delete().where(users.c.id == id))
        conn.commit()
        if result.rowcount == 0:
            raise HTTPException(status_code=404, detail="User not found")
        return {"message": "User deleted successfully"}
    except SQLAlchemyError as error:
        conn.rollback()
        raise HTTPException(status_code=500, detail=str(error))
