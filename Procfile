web: gunicorn HFC.wsgi --log-file -
worker: celery -A HFC worker --beat -l info -S django
