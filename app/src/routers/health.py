from fastapi import APIRouter

from ..domain.health import schemas

###
# Health Router configurations
###

router = APIRouter(tags=["health"])

@router.get("/health/check", response_model=schemas.HealthCheck)
def health_check():
  return schemas.HealthCheck(status="OK")
