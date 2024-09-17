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
SECRET_KEY = "2e045559d52ae605fa48270e4caf5df80f4bb36126738907a85ae857c9709893"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
