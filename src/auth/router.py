from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from src.dependencies import get_db, http_bearer
from src.auth.schemas import Token, AuthUser
from src.user.schemas import User
from src.auth.services import AuthService

router = APIRouter(tags=["auth"])

@router.post("/auth/token", response_model=Token)
def auth_user(form_data: AuthUser, db: Session = Depends(get_db)):
  auth_service = AuthService(db)
  return auth_service.authenticate(form_data.email, form_data.password)

@router.get("/auth/me", response_model=User)
def get_user_me(token: str = Depends(http_bearer), db: Session = Depends(get_db)):
  auth_service = AuthService(db)
  return auth_service.get_current_user(token)
