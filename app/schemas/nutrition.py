from pydantic import BaseModel, Field, ConfigDict
from typing import Optional
from datetime import datetime


class NutritionLogBase(BaseModel):
    meal_name : str  = Field(min_length=1, max_length=100)
    calories : float = Field(default=0.0, ge=0)
    proteins : float = Field(default=0.0, ge=0)
    carbs : float = Field(default=0.0, ge=0)
    fats : float = Field(default=0.0, ge=0)
    is_ai_generated : bool = False


class NutritionLogCreate(NutritionLogBase):
    logged_at: Optional[datetime] = None


# Schema for returning data (Response)
class NutritionLogResponse(NutritionLogBase):
    model_config = ConfigDict(from_attributes=True)
    id: int
    user_id: int
    logged_at: datetime