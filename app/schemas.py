from pydantic import BaseModel
from typing import Optional
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

class WorkflowUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    trigger_type: Optional[str] = None
    enabled: Optional[bool] = None