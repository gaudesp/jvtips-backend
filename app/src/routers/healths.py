from fastapi import APIRouter, status

from ..domain.health import schemas

###
# Health Router configurations
###

router = APIRouter(tags=["health"])

@router.get(
  "/health/",
  summary="Perform a Health Check",
  response_description="Return HTTP Status Code 200 (OK)",
  status_code=status.HTTP_200_OK,
  response_model=schemas.HealthCheck,
)
def get_health():
  return schemas.HealthCheck(status="OK")
