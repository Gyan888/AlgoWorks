from celery import Celery
import random
import redis
import json

app = Celery(
  broker='redis://redis:6379/0',
)


_db = redis.Redis(host="redis", port=6379)

def fibonaaci(number):
    series = (number+1) * [0]
    if number == 0:
        return 0

    series[1] = 1

    if number > 1:
        for i in range(2, number+1):
            series[i] = series[i-2] + series[i-1]

    return dict(zip(range(1, number+1), series))


class Task_B(app.Task):

    def run(self):
        keys = [key for key in _db.scan_iter() if key.isdigit()]
        if keys:
            for key in keys:
                print("series is -->", _db.get(key))
                _db.delete(key)
        else:
            print("No fibonacci series found.")



class Task_A(app.Task):

    def __init__(self, run_child=False):
        self.run_child = run_child

    def run(self):
        fibonaaci_number = random.randrange(1, 40)
        result = fibonaaci(fibonaaci_number)
        _db.set(fibonaaci_number, json.dumps(result))
        if self.run_child:
            b.delay()

task_a = Task_A(True)
task_b = Task_B()
a = app.register_task(task_a)
b = app.register_task(task_b)

app.conf.beat_schedule = {
    'run-every-10-seconds': {
        'task': 'tasks.Task_A',
        'schedule': 10,
    },
}

