
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict

app: FastAPI = FastAPI()
tasks: Dict[str, str] = {}

class Task(BaseModel):
    item: str
    status: str

# View Tasks
@app.get("/tasks/Task")
def view_task():
    if tasks:
        return tasks
    else:
        return{"message": "To-do list is empty."}

# Add Task
@app.post("/tasks")
def add_task(num: Task):
    if num.item in tasks:
        raise HTTPException(status_code=404, detail= "Task already exists.")
    else:
        tasks[num.item] = num.status
        return(view_task())

# Update Task
@app.put("/tasks/{item}")
def update_task(rep_item: str, new_item: Task):
    if rep_item not in tasks:
        raise HTTPException(status_code=404, detail="Task not found.")
    else:
        new_tasks: Dict = {}
        for i,j in tasks.items():
            if i==rep_item:
                new_tasks[new_item.item] = new_item.status
            else:
                new_tasks[i] = j
        tasks.clear()
        tasks.update(new_tasks)
        return(view_task())

# Delete Task
@app.delete("/tasks/{item}")
def delete_task(item: str):
    if item not in tasks:
        raise HTTPException(status_code= 404, detail= "Task not found.")
    else:
        del tasks[item]
        return(view_task())

# Clear List
@app.delete("/tasks")
def clear_list():
    if not tasks:
        raise HTTPException(status_code= 404, detail= "No tasks are found.")
    else:
        tasks.clear()
        return{"message": "Task list is empty"}