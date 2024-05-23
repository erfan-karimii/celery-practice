from kombu import Queue , Exchange

broker_url = 'pyamqp://guest@localhost//'

# List of modules to import when the Celery worker starts.
imports = ('proj.tasks',)

## Using the database to store task state and results.
result_backend = 'redis://localhost'

broker_connection_retry_on_startup=True

task_time_limit = 60
task_soft_time_limit = 50

worker_concurrency = 70 # for io bound tasks
worker_prefetch_multiplier = 4

# task_ignore_result = True
# task_store_errors_even_if_ignored = True

task_acks_late = True # set task acknowledged after finishing tasks

beat_schedule = {
    'add-every-30-seconds': {
        'task': 'tasks.adding',
        'schedule': 10.0,
        'args': (16, 16)
    },
},

default_exchange = Exchange('default',type='direct')
fanout_exchange = Exchange('f-exchange',type='direct')

task_queues = (
    Queue('default',    exchange='default'),
    Queue('feed_tasks', exchange='f-exchange'),
)

task_default_queue = 'default'
task_default_exchange = 'default'
task_default_routing_key = 'task.default'

# dont change execution poll in settings
# execution choices = 'solo':'heavy cpu task'
#                     'prefork':'cpu bound tasks'
#                     'eventlet':'io vound tasks'