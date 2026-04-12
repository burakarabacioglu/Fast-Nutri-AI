from pydantic import BaseModel, Field, EmailStr, ConfigDict


class UserRegister(BaseModel):
    username: str = Field(min_length=8, max_length=20, pattern="^[a-zA-Z0-9_]+$")
    first_name: str = Field(min_length=1, max_length=15)
    last_name: str = Field(min_length=1, max_length=30)
    email: EmailStr = Field(min_length=1, max_length=50)
    password: str = Field(min_length=8)

class UserResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    username: str
    first_name: str
    last_name: str
    email: EmailStr