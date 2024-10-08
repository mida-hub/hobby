from fastapi import status, HTTPException
from ..schemas import Blog, User
from .. import models
from sqlalchemy.orm import Session
from typing import Set

def fetch_all(db: Session):
    blogs = db.query(models.Blog).all()
    return blogs

def show(id: int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()

    if blog is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Blog with the id {id} is not available')

    return blog

def create(request: Blog, db: Session, current_user: Set[User]):
    # convert from set to list (exists only 1 element)
    user = list(current_user).pop()
    user_id = user.id

    new_blog = models.Blog(title=request.title, body=request.body, creator_id=user_id)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)

    return new_blog

def delete(id: int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    
    if blog.first() is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Blog with the id {id} is not found')

    blog.delete(synchronize_session=False)
    db.commit()

    return 'Deletion completed'

def update(id, request: Blog, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    
    if blog.first() is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Blog with the id {id} is not found')
    
    blog.update(request.dict())
    db.commit()

    return 'Update completed'
