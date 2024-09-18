from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from src.dependencies import get_db, http_bearer
from src.guide.schemas import Guide, GuideCreate, GuideList
from src.guide.services import GuideService

router = APIRouter(tags=["guides"])

@router.post("/guides", response_model=Guide)
def create_guide(data: GuideCreate, token: str = Depends(http_bearer), db: Session = Depends(get_db)):
  guide_service = GuideService(db, token)
  return guide_service.create(data)

@router.get("/guides", response_model=GuideList)
def get_guides(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
  guide_service = GuideService(db)
  return guide_service.get_all(skip, limit)

@router.get("/guides/{guide_id}", response_model=Guide)
def get_game(guide_id: int, db: Session = Depends(get_db)):
  guide_service = GuideService(db)
  guide = guide_service.get_by_id(guide_id)
  return guide
