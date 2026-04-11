from sqlalchemy.orm import relationship

from app.db.database import Base
from sqlalchemy import Column, Integer, String


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String, nullable=False, unique=True, index=True)
    password = Column(String)

    nutrition_logs = relationship("NutritionLog", back_populates="owner")
    user_profile = relationship("UserProfile", back_populates="user", uselist=False)