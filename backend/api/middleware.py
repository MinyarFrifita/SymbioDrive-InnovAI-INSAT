from fastapi import Request
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware
from datetime import datetime
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class RequestLoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        start_time = datetime.utcnow()
        
        # Log request
        logger.info(f"→ {request.method} {request.url.path}")
        
        try:
            response = await call_next(request)
        except Exception as e:
            logger.error(f"✗ Error: {str(e)}")
            return JSONResponse(
                status_code=500,
                content={"detail": "Internal server error"}
            )
        
        # Log response
        process_time = (datetime.utcnow() - start_time).total_seconds()
        logger.info(f"← {response.status_code} ({process_time:.3f}s)")
        
        response.headers["X-Process-Time"] = str(process_time)
        return response
