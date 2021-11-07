import uuid

from sqlalchemy.orm import Session

from app.core.domain.entities.event import EventCreate as EventCreateEntity
from app.core.models.event import Event


def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Event).offset(skip).limit(limit).all()

def create_user_item(db: Session, event: EventCreateEntity, user_uuid: uuid.UUID):
    db_event = Event(**event.dict(), owner_uuid=user_uuid)
    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    return db_event