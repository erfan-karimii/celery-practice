from .celery import app
from celery.utils.log import get_task_logger




@app.task(name='tasks.adding',bind=True)
def add(self,x, y):
    print(self.request)
    return x + y


@app.task(name='tasks.multiplying')
def mul(x, y):
    return x * y


@app.task(name='tasks.sum_of_elements')
def xsum(numbers):
    return sum(numbers)

@app.task(name='tasks.divisoning',bind=True,default_retry_delay=3)
def div(self,a,b):
    try:
        return a / b
    except ZeroDivisionError:
        self.retry(max_retries=10)
    