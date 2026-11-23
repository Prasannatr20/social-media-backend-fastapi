from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional

app= FastAPI()

my_posts=[{"title": "title of post 1", "content": "content of post", "id":1},
          {"title": "fav food", "content": "I like Biriyani", "id":2}]

@app.get("/")
async def root():
    return {"message": "Welcome to my API"}

@app.get("/posts")
def get_posts():
    return {"data":my_posts}



class Post(BaseModel):
    title:str
    content:str
    published: bool=True
    rating: Optional[int] = None

@app.post("/posts")
def create_posts(new_post: Post):
    print(new_post)
    print(new_post.content)
    print(new_post.title)
    print(new_post.published)
    print(new_post.rating)
    print(new_post.model_dump())
    return {"message":"Post created successfully"}