import uuid as uid
from typing import Optional

from pydantic import BaseModel


class EventBase(BaseModel):

    title: str
    description: Optional[str] = None


class EventCreate(EventBase):
    pass


class Event(EventBase):
    uuid: uid.UUID
    owner_uuid: uid.UUID

    class Config:
        orm_mode = True
