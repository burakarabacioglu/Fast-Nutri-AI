from sqlalchemy.orm import relationship

from app.db.database import Base
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Float, func


class NutritionLog(Base):
    __tablename__ = 'nutrition_logs'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), index=True, nullable=False)
    meal_name = Column(String, nullable=False)
    calories = Column(Float, default=0.0)
    proteins = Column(Float, default=0.0)
    carbs = Column(Float, default=0.0)
    fats = Column(Float, default=0.0)
    logged_at = Column(DateTime, nullable=False, default=func.now())
    is_ai_generated = Column(Boolean ,default=False)

    owner = relationship("User", back_populates="nutrition_logs")