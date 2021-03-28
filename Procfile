web: gunicorn HFC.wsgi --log-file -
worker: celery -A HFC worker -l info -B
