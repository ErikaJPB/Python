from fastapi import FastAPI
from routers import products, users, users_db, basic_auth_users, jwt_auth_users 
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Routers
app.include_router(products.router)
app.include_router(users.router)
app.include_router(basic_auth_users.router)
app.include_router(jwt_auth_users.router)
app.include_router(users_db.router)


# Static Resources
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def root():
    return "Hello FastAPI!"

@app.get("/url")
async def url():
    return {"url" : "https://developer-portfolio-ejpb.vercel.app/" }


# start the server : python -m uvicorn main:app --reload

# Swagger Documentation : http://127.0.0.1:8000/docs

# Redocly Documentation : http://127.0.0.1:8000/redoc