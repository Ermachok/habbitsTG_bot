from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime


class UserBase(BaseModel):
    name: str = Field(..., max_length=100)
    telegram_id: int
    is_active: Optional[bool] = True


class UserCreate(UserBase):
    password: str = Field(..., min_length=8)


class UserResponse(UserBase):
    id: int

    class Config:
        orm_mode = True


class HabitBase(BaseModel):
    name_habit: str = Field(..., max_length=100)
    description: Optional[str] = Field(None, max_length=255)


class HabitCreate(HabitBase):
    pass


class HabitResponse(HabitBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True


class HabitTrackingBase(BaseModel):
    habit_id: int
    alert_time: Optional[datetime] = None
    count: int = 0


class HabitTrackingCreate(HabitTrackingBase):
    pass


class HabitTrackingResponse(HabitTrackingBase):
    id: int

    class Config:
        orm_mode = True


class HabitWithTrackingResponse(HabitResponse):
    trackings: List[HabitTrackingResponse] = []

    class Config:
        orm_mode = True


class UserWithHabitsResponse(UserResponse):
    habits: List[HabitWithTrackingResponse] = []

    class Config:
        orm_mode = True
