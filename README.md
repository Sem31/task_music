1. git clone
2. create env
```
    python3 -m venv env
    source env/bin/activate
```
3. install req file
```
    pip install -r requirements.txt
```
4. run api 
```
    cd machineTest
    python manage.py migrate
    python manage.py createsuperuser
    python manage.py runserver
```

5. run test
```
    cd testcases
    pytest test_songAPI.py
```
