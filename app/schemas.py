from pydantic import BaseModel

class WorkFlowCreate(BaseModel):
    name: str
    description: str
    trigger_type: str
    enabled: bool