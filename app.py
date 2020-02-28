import time

import redis
from flask import Flask

app = Flask(__name__)
cache = redis.Redis(host='myredis', port=6379)


def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)


@app.route('/')
def hello():
    count = get_hit_count()
    return 'Myself Harry ,  I would be glad if it help you to understand how does docker compose and build image in docker works parallel with flask framework and redis as backend !!!!  Keep watching and enjoy the HIT COUNT !!! ------------->>>> {} times.\n'.format(count)

