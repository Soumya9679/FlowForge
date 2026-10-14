from fastapi import FastAPI, HTTPException
from app.schemas import WorkFlowCreate, WorkFlowResponse, WorkflowUpdate

app = FastAPI()

@app.get("/")
def read_root():
    return {"Message": "Application is healthy"}

workflows    : list[WorkFlowResponse]= []
@app.post("/workflows", response_model=WorkFlowResponse, status_code=201)
def create_workflow(workflow: WorkFlowCreate):
    workflow_data = WorkFlowResponse(
        id=len(workflows) + 1,
        name=workflow.name,
        description=workflow.description,
        trigger_type=workflow.trigger_type,
        enabled=workflow.enabled
    )
    workflows.append(workflow_data)
    return workflow_data

@app.get("/workflows", response_model=list[WorkFlowResponse])
def get_workflows():
    return workflows

@app.get("/workflows/{id}", response_model=WorkFlowResponse)
def get_workflow(id: int):
    for workflow in workflows:
        if workflow.id == id:
            return workflow
    raise HTTPException(status_code=404, detail="Workflow not found")

@app.patch("/workflows/{id}", response_model=WorkFlowResponse)
def update_workflow(id: int, workflow_update: WorkflowUpdate):
    for workflow in workflows:
        if workflow.id == id:
            update_data = workflow_update.model_dump(exclude_unset=True)
            for key, value in update_data.items():
                setattr(workflow, key, value)
            return workflow
    raise HTTPException(status_code=404, detail="Workflow not found")
