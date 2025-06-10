from fastapi import APIRouter, Depends
from fastapi.security import HTTPBearer

from src.api.v1.endpoints.auth_endpoints import router as auth_router
from src.api.v1.endpoints.server_endpoints import router as server_router
from src.api.v1.endpoints.user_endpoints import router as user_router
from src.security.auth.dependency import get_current_user
from src.utils.logger import logger

# -----------------------ROUTER--------------------
# API router for handling different endpoint routers
api_router = APIRouter()

# Include authentication-related routes
api_router.include_router(auth_router, tags=["AUTH Methods"])
# Include user-related routes with dependencies for security
api_router.include_router(
    user_router,
    tags=["USER Methods"],
    dependencies=[Depends(HTTPBearer()), Depends(get_current_user)],
)
# Include server-related routes
api_router.include_router(server_router, tags=["SERVER Methods"])

# Log the configuration of API routers
logger.info("🚀 API routers configured")