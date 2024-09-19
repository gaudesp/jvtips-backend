from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship
from src.database import Base

class User(Base):
  __tablename__ = "users"

  id = Column(Integer, primary_key=True, index=True)
  email = Column(String, unique=True, index=True)
  hashed_password = Column(String)
  disabled = Column(Boolean, default=False)

  guides = relationship("Guide", backref="user", lazy='dynamic')
