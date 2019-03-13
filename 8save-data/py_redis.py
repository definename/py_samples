import redis
conn = redis.Redis("localhost", 6379)

conn.keys("*")

# Need to install redis server