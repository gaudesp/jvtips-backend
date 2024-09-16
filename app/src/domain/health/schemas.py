from pydantic import BaseModel

###
# Health schemas
###

class HealthCheck(BaseModel):
  status: str = "OK"
