from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from src.dependencies import get_db, http_bearer
from src.pagination import Params
from src.guide.schemas import Guide, GuideCreate, Guides
from src.guide.services import GuideService

router = APIRouter(tags=["guides"])

@router.post("/guides", response_model=Guide)
def create_guide(data: GuideCreate, token: str = Depends(http_bearer), db: Session = Depends(get_db)):
  guide_service = GuideService(db, token)
  return guide_service.create(data)

@router.get("/guides", response_model=Guides)
def get_guides(params: Params = Depends(), db: Session = Depends(get_db)):
  guide_service = GuideService(db)
  return guide_service.get_all(params)

@router.get("/guides/{guide_id}", response_model=Guide)
def get_guide(guide_id: int, db: Session = Depends(get_db)):
  guide_service = GuideService(db)
  return guide_service.get_by_id(guide_id)
