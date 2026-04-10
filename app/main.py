from fastapi import FastAPI, HTTPException
from sqlalchemy import text
from app.db.database import engine
from app.models.users import Base
from app.api.deps import db_dependency
from app.api.v1.endpoints.auth import router as auth_router
from app.api.v1.endpoints.users import router as users_router


# Create the files before the app starts.
Base.metadata.create_all(engine)
app = FastAPI()
app.include_router(auth_router, prefix="/auth", tags=["Authentication"])
app.include_router(users_router, prefix="/users", tags=["Users"])


@app.get("/healthcheck")
async def healthcheck(db: db_dependency):
    try:
        # Simply ask the DB for the number 1 to verify connection
        db.execute(text("SELECT 1"))
        return {"status": "healthy", "database": "connected"}
    except Exception as e:
        raise HTTPException(status_code=503, detail="Database connection failed")
