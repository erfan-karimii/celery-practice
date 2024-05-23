from celery import Celery
from proj import celeryconfig

app = Celery('celery')
app.config_from_object(celeryconfig)

if __name__ == '__main__':
    app.start()
