from fastapi import APIRouter, Depends, status
from ..schemas import User, ShowUser
from ..database import get_db
from sqlalchemy.orm import Session
from ..functions import user

router = APIRouter(
    prefix='/user',
    tags=['users'],
)

@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=ShowUser)
def get_user(id: int, db: Session = Depends(get_db)):    
    return user.get_user(id, db)

@router.post('/', status_code=status.HTTP_201_CREATED)
def create_user(request: User, db: Session = Depends(get_db)):
    return user.create_user(request, db)
