# ref
## uploader
https://qiita.com/ekzemplaro/items/07abd9a941bcd0eb5834
https://github.com/JeremyFagis/dropify
https://dot-blog.jp/news/django-messages-frame-work/

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
