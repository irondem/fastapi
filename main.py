from fastapi import FastAPI, Response, status, HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

my_posts = [{"title": "title of post 1", "content": "content of post 1", "id": 1}, {"title": "favorite foods", "content": "I like pizza", "id": 2}]


def find_post(id):
    for p in my_posts:
        if p["id"] == id:
            return p


@app.get("/")
async def root():
    return {"message": "Welcome to my API!!!***"}

@app.get("/posts")
def get_posts():
    return {"data": my_posts}

@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_posts(post: Post):
    post_dict = post.model_dump()
    post_dict['id'] = randrange(0,10000000)
    my_posts.append (post_dict)
    return {"data" : post_dict}



@app.get("/posts/{id}")
def get_post(id: int):
    Post = find_post(id)
    if not Post:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,
                             detail={'message': f"post wiht: {id} was not found"} )
    return	{"post_detail" : Post}