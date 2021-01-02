# link-tracking
Track clicked links and report results to google sheets with all request arguments. I inspire on https://github.com/hyrsky/link-tracking then convert to flask and upgrade something

## Install instructions ##

1. Get Google Drive API credentials: https://gspread.readthedocs.io/en/latest/oauth2.html
2. Set ```GOOGLE_SHEETS_ID``` environment variable

```
virtualenv venv --python=python3.8
source venv/bin/activate
pip install -r requirements.txt
```

## Deploy ##
(inside virtualenv)
with gunicorn
```
gunicorn "index:app"
```
or with uwsgi
```
uwsgi --http 127.0.0.1:5000 --module index:app
```

## Testing ##

```
(inside virtualenv)
python index.py

curl -X GET -v "localhost:8000/?id=1337&val=666&url=https%3A%2F%2Fgoogle.com"
```
