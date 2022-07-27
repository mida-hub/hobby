from typing import List
from pydantic import BaseModel

class User(BaseModel):
    name: str
    email: str
    password: str

class Blog(BaseModel):
    title: str
    body: str
    creator_id: int

class RelationshipUser(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True

class RelationshipBlog(BaseModel):
    id: int
    title: str
    body: str

    class Config:
        orm_mode = True

class ShowUser(BaseModel):
    id: int
    name: str
    email: str
    blogs: List[RelationshipBlog] = []

    class Config:
        orm_mode = True

class ShowBlog(BaseModel):
    id: int
    title: str
    body: str
    user: RelationshipUser

    class Config:
        orm_mode = True
