# ref
https://pgmemo.tokyo/data/archives/982.html
https://blog1.mammb.com/entry/2019/12/11/090000

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
