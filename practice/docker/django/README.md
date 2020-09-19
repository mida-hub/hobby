# プロジェクト構成
```
django-admin startproject config .
```

# アプリケーション作成
```
python3 manage.py startapp accounts
```

# サーバー起動
```
python3 manage.py runserver 0.0.0.0:8000
python3 manage.py runserver 0.0.0.0:8000 --settings config.local_settings
```

# migrate
```
python manage.py makemigrations
python manage.py migrate
```

# OAuth
```
cf. https://qiita.com/moi1990sk/items/a849fca7acb29db95508
```
