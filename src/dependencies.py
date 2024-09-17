from src.database import SessionLocal
from passlib.context import CryptContext
from fastapi import HTTPException
from starlette.requests import Request
from starlette.responses import JSONResponse

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password, hashed_password):
  return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
  return pwd_context.hash(password)

def get_db():
  db = SessionLocal()
  try:
    yield db
  finally:
    db.close()

async def http_error_handler(_: Request, exc: HTTPException) -> JSONResponse:
  return JSONResponse({"errors": [exc.detail]}, status_code=exc.status_code)
