from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from backend.database.config import get_db
from backend.database.models import User, DrivingEvent
from backend.schemas import DrivingEventCreate, DrivingEventResponse
from backend.services.auth_service import AuthService

router = APIRouter(prefix="/api/driving-events", tags=["driving_events"])

def get_current_user(token: str, db: Session = Depends(get_db)) -> User:
    """Get current authenticated user from JWT token."""
    username = AuthService.decode_token(token)
    if not username:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials"
        )
    
    user = db.query(User).filter(User.username == username).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    return user

@router.post("/", response_model=DrivingEventResponse)
def create_driving_event(
    event: DrivingEventCreate,
    token: str,
    db: Session = Depends(get_db)
):
    """Record a new driving event."""
    user = get_current_user(token, db)
    
    db_event = DrivingEvent(
        user_id=user.id,
        event_type=event.event_type,
        severity=event.severity,
        latitude=event.latitude,
        longitude=event.longitude,
        speed=event.speed,
        acceleration=event.acceleration,
        notes=event.notes
    )
    
    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    
    return db_event

@router.get("/", response_model=List[DrivingEventResponse])
def get_driving_events(token: str, db: Session = Depends(get_db)):
    """Get all driving events for the authenticated user."""
    user = get_current_user(token, db)
    
    events = db.query(DrivingEvent).filter(
        DrivingEvent.user_id == user.id
    ).order_by(DrivingEvent.timestamp.desc()).all()
    
    return events

@router.get("/{event_id}", response_model=DrivingEventResponse)
def get_driving_event(event_id: int, token: str, db: Session = Depends(get_db)):
    """Get a specific driving event."""
    user = get_current_user(token, db)
    
    event = db.query(DrivingEvent).filter(
        (DrivingEvent.id == event_id) & (DrivingEvent.user_id == user.id)
    ).first()
    
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    
    return event
