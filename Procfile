web: gunicorn HFC.wsgi --log-file -
worker: celery -A HFC beat -l info
