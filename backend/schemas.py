from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

class UserBase(BaseModel):
    email: EmailStr
    username: str
    full_name: Optional[str] = None

class UserCreate(UserBase):
    password: str

class UserResponse(UserBase):
    id: int
    is_active: bool
    created_at: datetime
    
    class Config:
        from_attributes = True

class DrivingEventCreate(BaseModel):
    event_type: str
    severity: float
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    speed: Optional[float] = None
    acceleration: Optional[float] = None
    notes: Optional[str] = None

class DrivingEventResponse(DrivingEventCreate):
    id: int
    user_id: int
    timestamp: datetime
    created_at: datetime
    
    class Config:
        from_attributes = True

class DrivingStyleResponse(BaseModel):
    id: int
    user_id: int
    style_category: str
    confidence: float
    avg_speed: Optional[float] = None
    total_events: int
    harsh_events_count: int
    analysis_period_days: int
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True

class PredictionRequest(BaseModel):
    features: list[float]

class PredictionResponse(BaseModel):
    prediction: str
    confidence: float
    model_type: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None
