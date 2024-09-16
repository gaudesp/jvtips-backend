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
