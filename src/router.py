from fastapi import APIRouter
from src.health import router as health
from src.auth import router as auth
from src.user import router as user
from src.config import ROUTE_PREFIX

router = APIRouter()

def include_api_routes():
  router.include_router(health.router, prefix=ROUTE_PREFIX)
  router.include_router(auth.router, prefix=ROUTE_PREFIX)
  router.include_router(user.router, prefix=ROUTE_PREFIX)

include_api_routes()
