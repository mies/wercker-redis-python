import redis
import os

print 'testing'
print os.environ.get('WERCKER_REDIS_HOST', '127.0.0.1')

r = redis.StrictRedis(host=os.getenv("WERCKER_REDIS_HOST"), port=6379, db=0)
r.set('foo', 'bar')
result = r.get('foo')
assert result == 'bar'
