from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship
from sqlalchemy_utils import UUIDType

from app.core.models.database import Base


class Event(Base):
    __tablename__ = 'events'

    uuid = Column(UUIDType, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_uuid = Column(UUIDType, ForeignKey("users.uuid"))

    owner = relationship("User", back_populates="events")