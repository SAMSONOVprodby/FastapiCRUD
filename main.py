from uuid import uuid4

from fastapi import FastAPI, status, HTTPException
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
    completed: bool = False

class TaskCreate(BaseModel):
    title: str

class TaskUpdate(BaseModel):
    title: str | None = None
    completed: bool | None = None

tasks: list[Task] = []

@app.get('/tasks')
def get_tasks():
    return tasks

@app.post('/tasks', response_model=Task, status_code=status.HTTP_201_CREATED)
def add_task(payload: TaskCreate):
    task = Task(id=str(uuid4()), title=payload.title, completed=False)
    tasks.append(task)
    return task

@app.patch('/tasks/{task_id}', response_model=Task)
def patch_task(task_id: str, payload: TaskUpdate):
    for task in tasks:
        if task.id == task_id:
            if payload.title is not None:
                task.title = payload.title
            if payload.completed is not None:
                task.completed = payload.completed
            return task

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Задача не найдена')

@app.delete('/tasks/{task_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: str):
    for task in tasks:
        if task.id == task_id:
            tasks.remove(task)
            return f'Task has been successful removed'
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Задача не найдена')





# -----------------------------

class BaseCategory(BaseModel):
    name_category: str

class Category(BaseCategory):
    id: str

class CategoryCreate(BaseCategory):
    pass

class CategoryUpdate(BaseCategory):
    pass

categories: list[Category] = []

@app.get('/categories')
def get_categories():
    return categories

@app.post('/categories')
def post_categories(payload: Category):
    category = Category(id=str(uuid4()), name_category=payload.name_category)
    categories.append(category)
    return category

@app.patch('/categories/{category_id}')
def patch_categories(category_id: str, payload: CategoryUpdate):
    for category in categories:
        if category.id == category_id:
            if payload.name_category is not None:
                category.name_category = payload.name_category
            return category

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Категория не найдена')

@app.delete('/categories/{category_id}')
def delete_category(category_id: str):
    for category in categories:
        if category.id == category_id:
            categories.remove(category)
            return f'Task has been successful removed'
    
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Категория не найдена')
