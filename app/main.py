from fastapi import FastAPI
from app.db.database import engine
from app.models.users import Base

# Create the files before the app starts.
Base.metadata.create_all(engine)
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/healthcheck")
async def healthcheck():
    return {"status": "healthy"}
