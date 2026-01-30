from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class TaskRequest(BaseModel):
    task: str

@app.get("/")
def root():
    return {"status": "Konnex AI API running"}

@app.post("/infer")
def infer(req: TaskRequest):
    task = req.task.lower()

    steps_map = {
        "prepare groceries": [
            "Go to the kitchen",
            "Check grocery list",
            "Collect required items",
            "Pack items properly"
        ],
        "clean the table": [
            "Go to the table",
            "Remove objects",
            "Wipe surface",
            "Place items back"
        ]
    }

    steps = steps_map.get(task, [
        "Analyze task",
        "Break into steps",
        "Execute actions"
    ])

    return {
        "robot_policy": {
            "task": req.task,
            "sequence": [{"action": step} for step in steps]
        },
        "status": "ready"
    }
