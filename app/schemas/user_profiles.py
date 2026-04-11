from datetime import date, datetime
from typing import Optional
from pydantic import BaseModel, Field, ConfigDict
from app.models.user_profiles import GoalType, ActivityLevel

class UserProfileBase(BaseModel):
    age : int = Field(gt=0, lt=120)
    gender : Optional[str] = None
    height : float = Field(gt=0, description="Height in centimeters")
    weight : float = Field(gt=0, description="Weight in kilograms")
    body_fat: Optional[float] = Field(None, ge=2, lt=50)
    goal_type : GoalType = GoalType.MAINTENANCE
    target_weight: Optional[float] = Field(None, gt=0, description="Target weight in kilograms")
    target_date: Optional[date] = None
    activity_level : ActivityLevel = ActivityLevel.MODERATE

class UserProfileCreate(UserProfileBase):
    pass

class UserProfileResponse(UserProfileBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    user_id: int
    updated_at: datetime