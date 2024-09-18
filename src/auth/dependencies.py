import jwt
from jwt.exceptions import InvalidTokenError
from typing import Annotated
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from datetime import datetime, timedelta, timezone
from src.auth.config import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES
from src.auth.schemas import Token, TokenData

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def encode_access_token(data: dict) -> Token:
  to_encode = data.copy()
  expires_delta = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
  if expires_delta:
    expire = datetime.now(timezone.utc) + expires_delta
  else:
    expire = datetime.now(timezone.utc) + timedelta(minutes=15)
  to_encode.update({"exp": expire})
  encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
  token = Token(access_token=encoded_jwt)
  return token

def decode_access_token(token: Annotated[str, Depends(oauth2_scheme)]) -> TokenData:
  try:
    payload = jwt.decode(token.credentials, SECRET_KEY, algorithms=[ALGORITHM])
    email: str = payload.get("sub")
    if email is None:
      return
    token_data = TokenData(email=email)
  except InvalidTokenError:
    return
  return token_data
