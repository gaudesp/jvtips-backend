from sqlalchemy.orm import Session
from src.dependencies import get_password_hash
from src.guide.schemas import GuidesPaginated, Guides
from src.pagination import paginate, Params
from src.user.schemas import User, UserCreate, Users, UsersPaginated
from src.user.models import User as UserModel
from src.guide.models import Guide as GuideModel

class UserRepository:
  def __init__(self, db: Session):
    self.db = db

  def create(self, user: UserCreate) -> User:
    user = UserModel(email=user.email, hashed_password=get_password_hash(user.password))
    self.db.add(user)
    self.db.commit()
    self.db.refresh(user)
    return user

  def find_all(self, params: Params) -> Users:
    users = self.db.query(UserModel)
    paginated_users = paginate(users, params, UsersPaginated)
    return Users.model_validate(paginated_users)
  
  def find_one_by_id(self, user_id: int) -> User:
    user = self.db.query(UserModel).filter(UserModel.id == user_id).first()
    return user
  
  def find_one_by_email(self, email: str) -> User:
    user = self.db.query(UserModel).filter(UserModel.email == email).first()
    return user

  def find_guides(self, user: User, params: Params) -> Guides:
    guides = self.db.query(GuideModel).filter(GuideModel.user_id == user.id)
    paginated_guides = paginate(guides, params, GuidesPaginated)
    return Guides.model_validate(paginated_guides)
