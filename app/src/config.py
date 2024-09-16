from typing import List
from starlette.config import Config
from starlette.datastructures import CommaSeparatedStrings

###
# Properties configurations
###

config = Config(".env")

API_PREFIX = "/api"
ROUTE_PREFIX = "/v1"
ALLOWED_HOSTS: List[str] = config(
  "ALLOWED_HOSTS",
  cast=CommaSeparatedStrings,
  default="",
)
