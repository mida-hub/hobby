from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from ..database import get_db
from sqlalchemy.orm import Session
from ..functions import auth

router = APIRouter(
    tags=['Auth']
)

@router.post('/login')
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    return auth.login(request, db)
