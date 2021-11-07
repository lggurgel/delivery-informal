import uuid
from typing import List, Optional

from pydantic import BaseModel

from app.core.domain.entities.event import Event


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    uuid: uuid.UUID
    is_active: bool
    items: List[Event] = []

    class Config:
        orm_mode = True
