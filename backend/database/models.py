from datetime import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime, Boolean, ForeignKey, Text
from sqlalchemy.orm import relationship
from backend.database.config import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    full_name = Column(String, nullable=True)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    driving_events = relationship("DrivingEvent", back_populates="user")
    driving_styles = relationship("DrivingStyle", back_populates="user")

class DrivingEvent(Base):
    __tablename__ = "driving_events"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), index=True)
    event_type = Column(String)  # harsh_acceleration, harsh_braking, sharp_turn, etc.
    severity = Column(Float)  # 0-1 scale
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    speed = Column(Float, nullable=True)
    acceleration = Column(Float, nullable=True)
    notes = Column(Text, nullable=True)
    timestamp = Column(DateTime, default=datetime.utcnow)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Relationships
    user = relationship("User", back_populates="driving_events")

class DrivingStyle(Base):
    __tablename__ = "driving_styles"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), index=True)
    style_category = Column(String)  # aggressive, normal, cautious, etc.
    confidence = Column(Float)  # 0-1 confidence score
    avg_speed = Column(Float, nullable=True)
    total_events = Column(Integer, default=0)
    harsh_events_count = Column(Integer, default=0)
    analysis_period_days = Column(Integer)  # Number of days analyzed
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    user = relationship("User", back_populates="driving_styles")
