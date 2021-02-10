# cf.
- https://github.com/amaotone/fastapi-example

# setup
```
pipenv install fastapi
pipenv install uvicorn
pipenv install joblib
pipenv install sklearn
pipenv install palmerpenguins
pipenv install requests
pipenv install typing_extensions
pipenv install jinja2
pipenv install pytest
```

# run
```
pytest test_app.py
uvicorn main:app --reload
```

# curl
```
curl -X POST -d @test.json -H "Content-Type: application/json" localhost:8000/predict
```
