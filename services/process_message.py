from database import SessionLocal
from models import UserEvent

def save_event(user_id: int, intent: str):
    db = SessionLocal()
    event = UserEvent(user_id=user_id, intent=intent)
    db.add(event)
    db.commit()
    db.close()
