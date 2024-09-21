from sqlalchemy.orm import Session
from src.pagination import paginate, Params
from src.guide.schemas import Guide, GuideCreate, Guides, GuidesPaginated
from src.guide.models import Guide as GuideModel

class GuideRepository:
  def __init__(self, db: Session):
    self.db = db

  def create(self, guide: GuideCreate, user_id: int) -> Guide:
    guide = GuideModel(**guide.model_dump(), user_id=user_id)
    self.db.add(guide)
    self.db.commit()
    self.db.refresh(guide)
    return guide
  
  def find_all(self, params: Params) -> Guides:
    guides = self.db.query(GuideModel)
    paginated_guides = paginate(guides, params, GuidesPaginated)
    return Guides.from_orm(paginated_guides)
  
  def find_one_by_id(self, guide_id: int) -> Guide:
    guide = self.db.query(GuideModel).filter(GuideModel.id == guide_id).first()
    return guide
