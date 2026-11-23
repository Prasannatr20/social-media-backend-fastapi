from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange

app= FastAPI()

my_posts=[{"title": "title of post 1", "content": "content of post", "id":1},
          {"title": "fav food", "content": "I like Biriyani", "id":2}]

@app.get("/")
async def root():
    return {"message": "Welcome to my API"}

@app.get("/posts")
def get_posts():
    return {"data":my_posts}

def find_posts(id):
    for p in my_posts:
        if p["id"]== id:
            return p

class Post(BaseModel):
    title:str
    content:str
    published: bool=True
    rating: Optional[int] = None

@app.post("/posts")
def create_posts(new_post: Post):
    post_dict=new_post.model_dump()
    post_dict['id']=randrange(0,10000000)
    my_posts.append(post_dict)
    return {"data":post_dict}

@app.get("/posts/{id}")
def get_post(id: int):
    post=find_posts(id)
    return {"data": post}