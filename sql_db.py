from sqlalchemy import Select, create_engine
from sqlmodel import SQLModel, Field, Session
from typing import Optional
from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException


class Tasks(SQLModel, table=True):
    num: int = Field(default=None, primary_key= True)
    task: str 
    status: Optional[str]

connect_args = {"check_same_thread" : False}
engine = create_engine("sqlite:///database.db", echo = True, connect_args=connect_args)

def create_db_tables():
    SQLModel.metadata.create_all(engine)


@asynccontextmanager
async def lifespan(app: FastAPI):

    create_db_tables()
    yield

app= FastAPI(lifespan=lifespan)


@app.get("/")
def home():
     return {"msg":"hello world"}
# Add Task
@app.post("/tasks")
def add_task(task:Tasks):
    with Session(engine) as session:
        session.add(task)
        session.commit()
        #session.refresh(task)
        return {"Tasks":task}


@app.get("/tasks")
def view_task():
    with Session(engine) as session:
            return(session.exec(Select(Tasks)).all())
    