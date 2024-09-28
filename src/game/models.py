from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from src.database import Base

class Game(Base):
  __tablename__ = "games"

  id = Column(Integer, primary_key=True, index=True)
  name = Column(String, unique=True, index=True)
  igdb_id = Column(Integer, unique=True, index=True)

  guides = relationship("Guide", backref="game")
