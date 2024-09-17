from datetime import timedelta
from fastapi import Depends, HTTPException, status, APIRouter
from fastapi.security import HTTPBearer
from sqlalchemy.orm import Session

from ..dependencies import get_db
from ..domain.auth import services as auth_services, schemas as auth_schemas
from ..domain.user import schemas as user_schemas
from ..config import ACCESS_TOKEN_EXPIRE_MINUTES

security = HTTPBearer()
router = APIRouter(tags=["auth"])

@router.post("/auth/token", response_model=auth_schemas.Token)
def authenticate_user(form_data: auth_schemas.AuthenticateUser, db: Session = Depends(get_db)):
  user = auth_services.authenticate_user(db, form_data.email, form_data.password)
  access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
  access_token = auth_services.create_access_token(
    data={"sub": user.email}, expires_delta=access_token_expires
  )
  return auth_schemas.Token(access_token=access_token, token_type="bearer")

@router.get("/auth/me", response_model=user_schemas.User)
def get_users_me(token: str = Depends(security), db: Session = Depends(get_db)):
  current_user = auth_services.get_current_active_user(db, token)
  return current_user
