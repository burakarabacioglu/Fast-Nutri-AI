from pydantic import BaseModel, Field, EmailStr, ConfigDict


class UserRegister(BaseModel):
    first_name: str = Field(min_length=1, max_length=15)
    last_name: str = Field(min_length=1, max_length=30)
    email: EmailStr = Field(min_length=1, max_length=50)
    password: str = Field(min_length=8)

class UserResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    first_name: str
    last_name: str
    email: EmailStr