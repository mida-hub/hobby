# setup
pipenv shell
pipenv install fastapi uvicorn
pipenv install SQLAlchemy
pipenv install passlib bcrypt

# start
uvicorn main:app --reload
