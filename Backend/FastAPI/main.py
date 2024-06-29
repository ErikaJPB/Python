from fastapi import FastAPI
from routers import products, users

app = FastAPI()

# Routers
app.include_router(products.router)
app.include_router(users.router)

@app.get("/")
async def root():
    return "Hello FastAPI!"

@app.get("/url")
async def url():
    return {"url" : "https://developer-portfolio-ejpb.vercel.app/" }


# start the server : python -m uvicorn main:app --reload

# Swagger Documentation : http://127.0.0.1:8000/docs

# Redocly Documentation : http://127.0.0.1:8000/redoc