from fastapi import FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware
from starlette.exceptions import HTTPException

from .src.config import API_PREFIX, ALLOWED_HOSTS
from .src.database import engine, SessionLocal, Base
from .src.routers.api import router as router_api
from .src.routers.handlers.http_error import http_error_handler

###
# Main Application file
###

def get_application() -> FastAPI:
  # Start FastApi App 
  application = FastAPI()

  # Generate database tables
  Base.metadata.create_all(bind=engine)

  # Mapping api routes
  application.include_router(router_api, prefix=API_PREFIX)

  # Add exception handlers
  application.add_exception_handler(HTTPException, http_error_handler)

  # Allow cors
  application.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_HOSTS or ["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
  )

  return application

app = get_application()

# DB Session Middleware
# - create a new SQLAlchemy SessionLocal for each request
# - add it to the request
# - close it once the request is finished
@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
  response = Response("Internal server error", status_code=500)
  try:
    request.state.db = SessionLocal()
    response = await call_next(request)
  finally:
    request.state.db.close()
  return response
