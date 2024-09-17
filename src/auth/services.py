from typing import Annotated
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from src.dependencies import verify_password
from src.user.repositories import UserRepository
from src.user.schemas import User
from src.auth.schemas import Token
from src.auth.dependencies import oauth2_scheme, decode_access_token, encode_access_token

class AuthService:
  def __init__(self, db: Session):
    self.user_repository = UserRepository(db)

  def authenticate(self, email: str, password: str) -> Token:
    user = self.user_repository.find_one_by_email(email)
    if not user:
      raise HTTPException(status_code=401, detail="User not found")
    if not verify_password(password, user.hashed_password):
      raise HTTPException(status_code=401, detail="Incorrect email or password")
    access_token = encode_access_token(data={"sub": user.email})
    return access_token
  
  def get_current_user_by_token(self, token: Annotated[str, Depends(oauth2_scheme)]) -> User:
    token_data = decode_access_token(token)
    if token_data is None:
      raise HTTPException(status_code=401, detail="Could not validate credentials")
    user = self.user_repository.find_one_by_email(email=token_data.email)
    if not user:
      raise HTTPException(status_code=401, detail="User not found")
    if user.disabled:
      raise HTTPException(status_code=400, detail="User disabled")
    return user
