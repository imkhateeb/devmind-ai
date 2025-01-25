from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="Scalable Backend Project")

app.include_router(router)

@app.get("/")
async def root():
    return {"message": "Backend is up and running!"}
