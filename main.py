from fastapi import FastAPI
from app.schemas import WorkFlowCreate

app = FastAPI()

@app.get("/")
def read_root():
    return {"Message": "Application is healthy"}


@app.post("/workflows")
def create_workflow(workflow: WorkFlowCreate):
    return workflow
