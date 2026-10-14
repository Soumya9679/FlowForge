from fastapi import FastAPI, HTTPException
from app.schemas import WorkFlowCreate

app = FastAPI()

@app.get("/")
def read_root():
    return {"Message": "Application is healthy"}

workflows    = []
@app.post("/workflows")
def create_workflow(workflow: WorkFlowCreate):
    workflow = {
        "id": len(workflows) + 1,
        "name": workflow.name,
        "description": workflow.description,
        "trigger_type": workflow.trigger_type,
        "enabled": workflow.enabled
    }
    workflows.append(workflow)
    return workflow

@app.get("/workflows")
def get_workflows():
    return workflows

@app.get("/workflows/{id}")
def get_workflow(id: int):
    for workflow in workflows:
        if workflow["id"] == id:
            return workflow
    raise HTTPException(status_code=404, detail="Workflow not found")
