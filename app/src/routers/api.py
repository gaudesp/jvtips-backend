from fastapi import APIRouter

from . import healths, users
from ..config import ROUTE_PREFIX

###
# API Router configurations
###

router = APIRouter()

def include_api_routes():
  router.include_router(healths.router, prefix=ROUTE_PREFIX)
  router.include_router(users.router, prefix=ROUTE_PREFIX)

include_api_routes()
