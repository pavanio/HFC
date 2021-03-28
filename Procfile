web: gunicorn HFC.wsgi --log-file -
worker: celery -A HFC worker -l info
beat: celery -A HFC beat
