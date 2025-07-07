from fastapi import FastAPI, HTTPException, APIRouter
from datetime import datetime
from schema.classes import TodoCreate, TodoUpdate, Todo, todos, next_id
from typing import List
from fastapi import Query


router = APIRouter()


@router.post("/todos", response_model=Todo, status_code=201)
async def create_todo(todo: TodoCreate):
    global next_id
    new_todo = Todo(
        id=next_id,
        title=todo.title,
        description=todo.description,
        completed=False,
        created_at=datetime.now(),
        due_date=todo.due_date)
    todos.append(new_todo)
    next_id += 1
    return new_todo


#the endpoint to get all todos
@router.get("/todos")
async def get_all_todos():
    return todos


@router.get("/todos/filter", response_model=List[Todo])
async def filter_todos_by_status(completed: bool = Query(...)):
    return [todo for todo in todos if todo.completed == completed]


# the endpoint for getting todos by id
@router.get("/todos/{id}", response_model=Todo)
async def get_todo_by_id(id: int):
    for todo in todos:
        if todo.id == id:
            return todo
    raise HTTPException(status_code=404, detail="Todo not found")


#the endpoint to delet a todo by id
@router.delete("/todos/{id}")
async def delete_todo(id:int):
    for todo in todos:
        if todo.id == id:
            todos.remove(todo)
            return {"message": "Todo deleted"}
    raise HTTPException(status_code=404, detail="Todo not found")


#the endppoint to update a todo by id
@router.patch('/todos/{id}', response_model=Todo)
async def update_todo(id: int, update: TodoUpdate):
    for todo in todos:
        if todo.id == id:
            if update.title is not None:
                todo.title = update.title
            if update.description is not None:
                todo.description = update.description
            if update.completed is not None:
                todo.completed = update.completed
            if update.due_date is not None:
                todo.due_date = update.due_date
            return todo
        raise HTTPException(status_code=404, detail="Todo not found")
    

#the endpoint to mark a todo as completed
@router.patch('/todos/{id}/completed', response_model=Todo)
async def mark_todo_completed(id: int):
    for todo in todos:
        if todo.id == id:
            todo.completed =True
            print(f"Tentative de marquer le todo {id} comme terminé.")
            return todo
    raise HTTPException(status_code=404, detail="Todo not found")
