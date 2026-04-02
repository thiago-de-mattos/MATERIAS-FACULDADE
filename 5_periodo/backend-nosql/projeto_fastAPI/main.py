from fastapi import FastAPI
from routes.user_route import router

app = FastAPI()

app.include_router(router)

@app.get("/")
def home():
    return {"Message": "FastAPI + MongoDB + Docker"}