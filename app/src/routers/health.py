from fastapi import APIRouter

from app.src.domain.health.schemas import HealthCheck

router = APIRouter(tags=["health"])

@router.get("/health/check", response_model=HealthCheck)
def health_check():
  return HealthCheck()
