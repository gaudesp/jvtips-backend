from fastapi import APIRouter

from . import health
from ..config import ROUTE_PREFIX

###
# API Router configurations
###

router = APIRouter()

def include_api_routes():
  router.include_router(health.router, prefix=ROUTE_PREFIX)

include_api_routes()
