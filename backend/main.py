from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from config import settings
from backend.database.config import engine, Base
from backend.database import models
from backend.api.routes import auth, driving_events, predictions
from backend.api.middleware import RequestLoggingMiddleware

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Driving Behavior API",
    description="API for tracking and predicting driving behavior",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(RequestLoggingMiddleware)

app.include_router(auth.router)
app.include_router(driving_events.router)
app.include_router(predictions.router)

@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "api_version": "1.0.0"
    }

@app.get("/")
def root():
    return {
        "message": "Driving Behavior API",
        "docs": "/docs",
        "openapi": "/openapi.json"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        app,
        host=settings.API_HOST,
        port=settings.API_PORT,
        reload=settings.DEBUG
    )
