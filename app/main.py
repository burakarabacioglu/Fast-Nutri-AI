from fastapi import FastAPI
from app.db.database import engine, SessionLocal
from app.models.users import Base

# Create the files before the app starts.
Base.metadata.create_all(engine)
app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/healthcheck")
async def healthcheck():
    return {"status": "healthy"}
