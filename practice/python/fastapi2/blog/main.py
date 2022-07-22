from fastapi import FastAPI
from starlette.responses import FileResponse
from .schemas import Blog

app = FastAPI()
favicon_path = 'favicon.ico'

@app.get('/favicon.ico')
async def favicon():
    return FileResponse(favicon_path)

@app.post('/blog')
def create(blog: Blog):
    return {'data': blog}
