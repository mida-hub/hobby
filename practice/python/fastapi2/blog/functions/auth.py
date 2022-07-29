from fastapi import status, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from .. import models, token
from ..hashing import Hash
from sqlalchemy.orm import Session

def login(request: OAuth2PasswordRequestForm, db: Session):
    user = db.query(models.User).filter(models.User.email == request.username).first()

    if user is None:
        HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                      detail=f'Invalid Credentials')
    
    if not Hash.verify(request.password, user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Incorrect password')

    access_token = token.create_access_token(
        data={"sub": user.email, "id": user.id}
    )

    return {"access_token": access_token, "token_type": "bearer"}
