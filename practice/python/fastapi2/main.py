from fastapi import FastAPI
from starlette.responses import FileResponse
from typing import Optional
from pydantic import BaseModel

class Blog(BaseModel):
    title: str
    description: str
    published_at: Optional[bool]


app = FastAPI()
favicon_path = 'favicon.ico'

@app.get('/')
def index():
    return {'data': {'name': 'Test'}}

@app.get('/favicon.ico')
async def favicon():
    return FileResponse(favicon_path)

@app.get('/user/{id}')
def get_user(id):
    return {'data': id}

@app.get('/blog')
def item(limit=10, published: bool=True):
    if published:
        return {'data': f'{limit}件'}
    else:
        return {'data': '非公開'}

@app.post('/blog')
def create_blog(blog: Blog):
    return {'data': blog}
