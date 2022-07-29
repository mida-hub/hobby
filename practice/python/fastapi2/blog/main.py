from fastapi import FastAPI
from .models import Base
from .database import engine
from .routes import auth, blog, user

app = FastAPI()
app.include_router(auth.router)
app.include_router(blog.router)
app.include_router(user.router)

Base.metadata.create_all(engine)
