# setup
```
pipenv install -r ./requirements.txt
mkdir uploader
cd uploader
django-admin startproject config .
django-admin startapp web
python manage.py migrate
python manage.py makemigrations
python manage.py runserver
```
