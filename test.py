import redis
import os

print 'testing'
r = redis.StrictRedis(host=os.getenv("WERCKER_REDIS_HOST"), port=6379, db=0)
r.set('foo', 'bar')
result = r.get('foo')
assert result == 'bar'
print result
