from fastapi import FastAPI, Path, HTTPException
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

tasks = {
    1: {
        "Work" : "FastAPI Video",
        "Status" : "Done"
    },
    2: {
        "Work" : "TaskAPI",
        "Status" : "On-Going"
    }
}

class Task(BaseModel):
    Work : str
    Status : str

class UpdateTask(BaseModel):
    Work : Optional[str] = None
    Status : Optional[str] = None


@app.get("/")
def list_all():
    return list(tasks.values())

@app.get("/task-by-id/{task_id}")
def list_by_id(task_id: int = Path(..., description="Enter task Id")):
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task Not Found")
    
    return tasks[task_id]

@app.get("/task-by-work")
def list_by_name(work : str):
    for task_id in tasks:
        if tasks[task_id]["Work"] == work:
            return tasks[task_id]
    raise HTTPException(status_code=404, detail="Task Not Found")
    

@app.post("/create-task/{task_id}")
def create_task(task_id : int, task : Task):
    if task_id in tasks:
        raise HTTPException(status_code=409, detail="Task already exists")

    tasks[task_id] = task.model_dump()
    return [f"Task number {task_id} was created", tasks[task_id]]

@app.put("/update-task/{task_id}")
def update_task(task_id : int, task : UpdateTask):
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task Not Found")

    if task.Work is not None:
        tasks[task_id]["Work"] = task.Work 

    if task.Status is not None:
        tasks[task_id]["Status"] = task.Status 

    return tasks[task_id]


@app.delete("/delete-task/{task_id}")
def delete_task(task_id: int):
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task Not Found")

    del tasks[task_id]
    return {"Message" : "Task deleted successfully"}