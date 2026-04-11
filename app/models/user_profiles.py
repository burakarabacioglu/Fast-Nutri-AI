import enum
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Float, Enum as SqlEnum
from app.db.database import Base

class GoalType(str, enum.Enum):
    LOSE_FAT = "Lose Fat"
    GAIN_MUSCLE = "Gain Muscle"
    MAINTENANCE = "Maintenance"

class ActivityLevel(str, enum.Enum):
    SEDENTARY = "Sedentary"
    MODERATE = "Moderate"
    ACTIVE = "Active"

class UserProfile(Base):
    __tablename__ = 'user_profiles'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    age = Column(Integer)
    gender = Column(String)
    height = Column(Float)
    weight = Column(Float)
    body_fat = Column(Float)
    goal_type = Column(SqlEnum(GoalType))
    target_weight = Column(Float)
    target_date = Column(DateTime)
    activity_level = Column(SqlEnum(ActivityLevel))
    updated_at = Column(DateTime)