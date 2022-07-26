import imp
import re
from fastapi import FastAPI, Depends, status, Response, HTTPException
from starlette.responses import FileResponse
from typing import List
from .schemas import Blog, ShowBlog, User, ShowUser
from .models import Base
from . import models
from .database import engine, sessionLocal
from .hashing import Hash
from sqlalchemy.orm import Session

app = FastAPI()
favicon_path = 'favicon.ico'
Base.metadata.create_all(engine)

def get_db():
    db = sessionLocal()

    try:
        yield db
    finally:
        db.close()

@app.get('/favicon.ico')
async def favicon():
    return FileResponse(favicon_path)

@app.post('/blog', status_code=status.HTTP_201_CREATED, tags=['blogs'])
def create(blog: Blog, db: Session = Depends(get_db)):
    new_blog = models.Blog(title=blog.title, body=blog.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)

    return new_blog

@app.get('/blog', response_model=List[ShowBlog], tags=['blogs'])
def all_fetch(db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs

@app.get('/blog/{id}', status_code=status.HTTP_200_OK, response_model=ShowBlog, tags=['blogs'])
def show(id: int, response: Response, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()

    if blog is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Blog with the id {id} is not available')
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {'detail': f'Blog with the id {id} is not available'}

    return blog

@app.delete('/blog/{id}', status_code=status.HTTP_204_NO_CONTENT, tags=['blogs'])
def delete(id: int, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    
    if blog.first() is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Blog with the id {id} is not found')

    blog.delete(synchronize_session=False)
    db.commit()

    return 'Deletion completed'

@app.put('/bloh/{id}', status_code=status.HTTP_202_ACCEPTED, tags=['blogs'])
def update(id, request: Blog, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    
    if blog.first() is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Blog with the id {id} is not found')
    
    blog.update(request.dict())
    db.commit()

    return 'Update completed'

@app.post('/user', status_code=status.HTTP_201_CREATED, tags=['users'])
def create_user(request: User, db: Session = Depends(get_db)):
    hashed_password = Hash.bcrypt(request.password)

    new_user = models.User(name=request.name,
                           email=request.email,
                           password=hashed_password)

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

@app.get('/user/{id}', status_code=status.HTTP_200_OK, response_model=ShowUser, tags=['users'])
def get_user(id: int, response: Response, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()

    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'User with the id {id} is not available')

    return user
