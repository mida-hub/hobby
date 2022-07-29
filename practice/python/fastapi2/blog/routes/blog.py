from typing import List
from fastapi import APIRouter, Depends, status
from ..schemas import Blog, ShowBlog, User
from ..database import get_db
from .. import oauth2
from sqlalchemy.orm import Session
from ..functions import blog

router = APIRouter(
    prefix='/blog',
    tags=['blogs'],
)

@router.get('/', response_model=List[ShowBlog])
def fetch_all(db: Session = Depends(get_db),
              current_user: User = Depends(oauth2.get_current_user)):
    return blog.fetch_all(db)

@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=ShowBlog)
def show(id: int, db: Session = Depends(get_db)):
    return blog.show(id, db)

@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: Blog,
           db: Session = Depends(get_db),
           current_user: User = Depends(oauth2.get_current_user)):
    return blog.create(request, db, current_user)

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete(id: int, db: Session = Depends(get_db)):   
    return blog.delete(id, db)

@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id, request: Blog, db: Session = Depends(get_db)):
    return blog.update(id, request, db)
