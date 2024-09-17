from fastapi import FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware
from starlette.exceptions import HTTPException
from app.src.config import API_PREFIX, ALLOWED_HOSTS
from app.src.database import engine, SessionLocal, Base
from app.src.router import router as router_api
from app.src.dependencies import http_error_handler

def get_application() -> FastAPI:
  application = FastAPI()
  Base.metadata.create_all(bind=engine)
  application.include_router(router_api, prefix=API_PREFIX)
  application.add_exception_handler(HTTPException, http_error_handler)
  application.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_HOSTS or ["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
  )
  return application

app = get_application()

@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
  response = Response("Internal server error", status_code=500)
  try:
    request.state.db = SessionLocal()
    response = await call_next(request)
  finally:
    request.state.db.close()
  return response
