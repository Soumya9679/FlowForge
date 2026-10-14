from pydantic import BaseModel

class WorkFlowCreate(BaseModel):
    name: str
    description: str
    trigger_type: str
    enabled: bool

class WorkFlowResponse(BaseModel):
    id: int
    name: str
    description: str
    trigger_type: str
    enabled: bool