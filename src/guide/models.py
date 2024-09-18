from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from src.database import Base

class Guide(Base):
  __tablename__ = "guides"

  id = Column(Integer, primary_key=True, index=True)
  title = Column(String)
  description = Column(String)
  content = Column(Text)
  game_id = Column(Integer, ForeignKey("games.id"))
  user_id = Column(Integer, ForeignKey("users.id"))
