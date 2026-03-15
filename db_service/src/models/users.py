"""
Модуль для описания модели пользователя.
"""

from datetime import date, datetime
from enum import Enum

from pydantic import BaseModel, EmailStr


class UserRole(Enum):
    """
    Перечисление ролей пользователя.
    """

    ADMIN = "admin"
    USER = "user"
    SELLER = "seller"


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
    role: UserRole
