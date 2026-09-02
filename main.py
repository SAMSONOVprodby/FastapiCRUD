from uuid import uuid4

from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        'http://localhost:3000',
    ],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

class Task(BaseModel):
    id: str
    title: str
    complited: bool = False

class TaskCreate(BaseModel):
    title: str

tasks: list[Task] = []

@app.get('/tasks')
def get_tasks():
    return tasks

@app.post('/tasks', response_model=Task, status_code=status.HTTP_201_CREATED)
def add_task(payload: TaskCreate):
    task = Task(id=str(uuid4()), title=payload.title, complited=False)
    tasks.append(task)
    return task