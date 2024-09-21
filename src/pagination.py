from fastapi import Query
from pydantic import BaseModel
from typing import Type, TypeVar, Generic, List, Dict, Any
from pydantic import BaseModel

T = TypeVar("T", bound=BaseModel)

class Params(BaseModel):
  page: int = Query(1, ge=1, description="Page number")
  size: int = Query(50, ge=1, le=100, description="Page size")

class Paginated(BaseModel, Generic[T]):
  total_items: int
  total_pages: int
  current_page: int
  page_size: int
  items: List[T]

class ORMNestedMixin(BaseModel):
  @classmethod
  def from_orm_nested(cls, parent_data, **nested_data: Paginated):
    parent_model = next(base for base in cls.__bases__ if issubclass(base, BaseModel))
    model_data = parent_model.from_orm(parent_data)
    return cls(**model_data.dict(), **nested_data)

def paginate(query, params: Params, schema: Type[Paginated[T]]) -> Paginated[T]:
  total_items = query.order_by(None).count()
  items = query.offset((params.page - 1) * params.size).limit(params.size).all()
  total_pages = (total_items + params.size - 1) // params.size
  items = [schema.items_model.from_orm(item) for item in items]

  return schema(
    total_items=total_items,
    total_pages=total_pages,
    current_page=params.page,
    page_size=params.size,
    items=items
  )
