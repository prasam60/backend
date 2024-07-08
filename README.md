## Get started

1. Install dependencies

```
pip install -r requirements.txt
```

2. Update `ALLOWED_HOSTS`, if using expo go app for Front-end. Open `settings.py` and add IP address to `ALLOWED_HOSTS`.

```
ALLOWED_HOSTS = ['localhost', '192.168.1.8']
```

2. Start server

```
python manage.py runserver 0.0.0.0:8000
```


## Future Work

1. Create separate table for Roles and add FK to memeber table.
2. Authentication / Authorization. 
3. Add tests.