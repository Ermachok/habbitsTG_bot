from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Text, TIMESTAMP
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    telegram_id = Column(Integer, unique=True, nullable=False)
    password = Column(Text, nullable=False)

    habits = relationship("Habit", back_populates="user")


class Habit(Base):
    __tablename__ = "habits"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    name_habit = Column(String, nullable=False)
    description = Column(String, nullable=True)

    user = relationship("User", back_populates="habits")
    trackings = relationship("HabitTracking", back_populates="habit")


class HabitTracking(Base):
    __tablename__ = "habittrackings"

    id = Column(Integer, primary_key=True, autoincrement=True)
    habit_id = Column(Integer, ForeignKey("habits.id"), nullable=False)
    alert_time = Column(TIMESTAMP(timezone=True), nullable=True)
    count = Column(Integer, default=0)

    habit = relationship("Habit", back_populates="trackings")
