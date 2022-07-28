from fastapi import APIRouter, Depends, status, Response, HTTPException
from ..schemas import User, ShowUser
from .. import models
from ..database import get_db
from ..hashing import Hash
from sqlalchemy.orm import Session

router = APIRouter(
    prefix='/user',
    tags=['users'],
)

@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=ShowUser)
def get_user(id: int, response: Response, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()

    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'User with the id {id} is not available')

    return user

@router.post('/', status_code=status.HTTP_201_CREATED)
def create_user(request: User, db: Session = Depends(get_db)):
    hashed_password = Hash.bcrypt(request.password)

    new_user = models.User(name=request.name,
                           email=request.email,
                           password=hashed_password)

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user
