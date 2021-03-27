web: gunicorn HFC.wsgi --log-file -
worker: celery -A HFC worker -B -E --loglevel=info
