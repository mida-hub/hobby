# setup
pipenv shell
pipenv install fastapi uvicorn
pipenv install SQLAlchemy

# start
uvicorn main:app --reload
