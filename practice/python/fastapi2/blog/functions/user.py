from fastapi import status, HTTPException
from ..schemas import User
from .. import models
from ..hashing import Hash
from sqlalchemy.orm import Session

def get_user(id: int, db: Session):
    user = db.query(models.User).filter(models.User.id == id).first()

    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'User with the id {id} is not available')

    return user

def create_user(request: User, db: Session):
    hashed_password = Hash.bcrypt(request.password)

    new_user = models.User(name=request.name,
                           email=request.email,
                           password=hashed_password)

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user
