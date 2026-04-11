import enum
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Float, Enum as SqlEnum, Date, func
from sqlalchemy.orm import relationship

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
    user_id = Column(Integer, ForeignKey('users.id'), unique=True, index=True)
    age = Column(Integer, nullable=False)
    gender = Column(String)
    height = Column(Float, nullable=False)
    weight = Column(Float, nullable=False)
    body_fat = Column(Float)
    goal_type = Column(SqlEnum(GoalType))
    target_weight = Column(Float)
    target_date = Column(Date)
    activity_level = Column(SqlEnum(ActivityLevel))
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    user = relationship("User", back_populates="user_profile")