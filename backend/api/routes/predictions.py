from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from backend.database.config import get_db
from backend.database.models import User, DrivingStyle
from backend.schemas import PredictionRequest, PredictionResponse, DrivingStyleResponse
from backend.services.ml_service import ml_service
from backend.services.auth_service import AuthService
from datetime import datetime

router = APIRouter(prefix="/api/predictions", tags=["predictions"])

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

@router.post("/driving-event", response_model=PredictionResponse)
def predict_driving_event(
    request: PredictionRequest,
    token: str,
    db: Session = Depends(get_db)
):
    """Predict driving event type from features."""
    user = get_current_user(token, db)
    
    result = ml_service.predict_driving_event(request.features)
    
    if "error" in result:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=result["error"]
        )
    
    return result

@router.post("/driving-style", response_model=PredictionResponse)
def predict_driving_style(
    request: PredictionRequest,
    token: str,
    db: Session = Depends(get_db)
):
    """Predict driving style from features."""
    user = get_current_user(token, db)
    
    result = ml_service.predict_driving_style(request.features)
    
    if "error" in result:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=result["error"]
        )
    
    return result

@router.post("/driving-style/save", response_model=DrivingStyleResponse)
def save_driving_style(
    style_category: str,
    confidence: float,
    avg_speed: float = None,
    total_events: int = 0,
    harsh_events_count: int = 0,
    analysis_period_days: int = 7,
    token: str = None,
    db: Session = Depends(get_db)
):
    """Save driving style analysis to database."""
    if token is None:
        raise HTTPException(status_code=401, detail="Token required")

    user = get_current_user(token, db)
    
    db_style = DrivingStyle(
        user_id=user.id,
        style_category=style_category,
        confidence=confidence,
        avg_speed=avg_speed,
        total_events=total_events,
        harsh_events_count=harsh_events_count,
        analysis_period_days=analysis_period_days
    )
    
    db.add(db_style)
    db.commit()
    db.refresh(db_style)
    
    return db_style

@router.get("/driving-style/latest", response_model=DrivingStyleResponse)
def get_latest_driving_style(token: str, db: Session = Depends(get_db)):
    """Get the latest driving style analysis for the user."""
    user = get_current_user(token, db)
    
    style = db.query(DrivingStyle).filter(
        DrivingStyle.user_id == user.id
    ).order_by(DrivingStyle.created_at.desc()).first()
    
    if not style:
        raise HTTPException(status_code=404, detail="No style analysis found")
    
    return style
