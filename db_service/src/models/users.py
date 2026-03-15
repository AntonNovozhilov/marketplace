"""
Модуль для описания модели пользователя.
"""

from pydantic import BaseModel, EmailStr
from datetime import date, datetime


class User(BaseModel):
    """
    Модель пользователя.
    """
    
    id: int
    name: str
    surname: str
    email: EmailStr
    phone: str
    password: str
    date_of_birth: date
    is_active: bool
    created_at: datetime
    updated_at: datetime
    deleted_at: datetime



    