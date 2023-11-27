from fastapi import FastAPI, Response, status, HTTPException, Depends
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from sqlalchemy.orm import Session
from . import models
from .database import engine, get_db


models.Base.metadata.create_all(bind=engine)



app = FastAPI()



class Post(BaseModel):
    title: str
    content: str
    published: bool = True


while True:

    try:
        conn = psycopg2.connect(host = 'localhost', database = 'fastapi', user='postgres',
                                password = 'Tech_123', cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print ("Database connection was successfull!")
        break
    except Exception as error:
        print("Connecting to database failed")
        print("Error: ", error)
        time.sleep(2)
        
app.get("/sqlachemy")
def test_posts(db: Session = Depends(get_db)):

    posts = db.query(models.Post).all()

    print(posts)
    return {"data":"successfull"}




my_posts = [{"title": "title of post 1", "content": "content of post 1", "id": 1},
            {"title": "favorite foods", "content": "I like pizza", "id": 2}]


def find_post(id):
    for p in my_posts:
        if p["id"] == id:
            return p


def find_index_post(id):
    for i, p in enumerate(my_posts):
        if p['id'] == id:
            return i


@app.get("/")
async def root():
    return {"message": "Welcome to my API!!!***"}


@app.get("/posts")
def get_posts(db: Session = Depends(get_db)):
    posts = db.query(models.Post).all()
    return {"data": posts}


@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_post(post: Post, db: Session = Depends(get_db)):

    new_post = models.Post(**post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return {"data": new_post}

