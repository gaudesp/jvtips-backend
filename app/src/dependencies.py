import bcrypt
from .database import SessionLocal

###
# Dependencies configurations
###

def get_db():
  db = SessionLocal()
  try:
    yield db
  finally:
    db.close()

def hash_password(password):
  password_bytes = password.encode('utf-8')
  hashed_bytes = bcrypt.hashpw(password_bytes, bcrypt.gensalt())
  return hashed_bytes.decode('utf-8')
