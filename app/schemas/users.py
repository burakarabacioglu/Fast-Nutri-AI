from pydantic import BaseModel, Field

class UserRegister(BaseModel):
    first_name: str = Field(min_length=1, max_length=15)
    last_name: str = Field(min_length=1, max_length=30)
    email: str
    password: str
    bodyfat: float