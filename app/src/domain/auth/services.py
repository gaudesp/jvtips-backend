import jwt

from datetime import datetime, timedelta, timezone
from typing import Annotated
from fastapi import Depends, HTTPException, status
from jwt.exceptions import InvalidTokenError
from sqlalchemy.orm import Session

from ..auth import schemas as auth_schemas
from ..user import services as user_services
from ...config import SECRET_KEY, ALGORITHM
from ...dependencies import verify_password, oauth2_scheme

def authenticate_user(db: Session, email: str, password: str):
  authenticate_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Incorrect email or password",
    headers={"WWW-Authenticate": "Bearer"},
  )
  user = user_services.get_user_by_email(db, email)
  if not user:
    raise authenticate_exception
  if not verify_password(password, user.hashed_password):
    raise authenticate_exception
  return user

def create_access_token(data: dict, expires_delta: timedelta | None = None):
  to_encode = data.copy()
  if expires_delta:
    expire = datetime.now(timezone.utc) + expires_delta
  else:
    expire = datetime.now(timezone.utc) + timedelta(minutes=15)
  to_encode.update({"exp": expire})
  encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
  return encoded_jwt

def get_current_user(db: Session, token: Annotated[str, Depends(oauth2_scheme)]):
  credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Could not validate credentials",
    headers={"WWW-Authenticate": "Bearer"},
  )
  try:
    payload = jwt.decode(token.credentials, SECRET_KEY, algorithms=[ALGORITHM])
    email: str = payload.get("sub")
    if email is None:
      raise credentials_exception
    token_data = auth_schemas.TokenData(email=email)
  except InvalidTokenError:
    raise credentials_exception
  user = user_services.get_user_by_email(db, email=token_data.email)
  if user is None:
    raise credentials_exception
  return user

def get_current_active_user(db: Session, token: Annotated[str, Depends(oauth2_scheme)]):
  current_user = get_current_user(db, token)
  if not current_user.is_active:
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
      detail="Inactive user",
      headers={"WWW-Authenticate": "Bearer"}
    )
  return current_user
