from sqlalchemy import Boolean, Column, String
from sqlalchemy.orm import relationship
from sqlalchemy_utils import UUIDType, EmailType

from app.core.models.database import Base


class User(Base):
    __tablename__ = 'users'

    uuid = Column(UUIDType, primary_key=True, index=True)
    email = Column(EmailType, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    events = relationship("Event", back_populates="owner")
