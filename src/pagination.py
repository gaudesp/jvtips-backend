from fastapi import Query
from pydantic import BaseModel

class Params(BaseModel):
  page: int = Query(1, ge=1, description="Page number")
  size: int = Query(50, ge=1, le=100, description="Page size")

class Paginated(BaseModel):
  total_items: int
  total_pages: int
  current_page: int
  page_size: int

def paginate(query, params, schema):
  total_items = query.order_by(None).count()
  items = query.offset((params.page - 1) * params.size).limit(params.size).all()
  total_pages = (total_items + params.size - 1) // params.size

  return schema(items=items, total_items=total_items, total_pages=total_pages, current_page=params.page, page_size=params.size)
