# setup
pipenv shell
pipenv install fastapi uvicorn
pipenv install SQLAlchemy
pipenv install passlib bcrypt
pipenv install python-jose
pipenv install python-dotenv
pipenv install python-multipart

# start
uvicorn main:app --reload

# jwt
openssl rand -hex 32
