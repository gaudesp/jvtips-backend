from typing import List
from starlette.config import Config
from starlette.datastructures import CommaSeparatedStrings

config = Config(".env")

API_PREFIX = "/api"
ROUTE_PREFIX = "/v1"
ALLOWED_HOSTS: List[str] = config(
  "ALLOWED_HOSTS",
  cast=CommaSeparatedStrings,
  default="",
)
POSTGRES_USER = config('POSTGRES_USER')
POSTGRES_PASSWORD = config('POSTGRES_PASSWORD')
POSTGRES_PORT = config('POSTGRES_PORT')
POSTGRES_HOST = config('POSTGRES_HOST')
POSTGRES_DB = config('POSTGRES_DB')
DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
