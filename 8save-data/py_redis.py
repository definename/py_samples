
import redis
conn = redis.Redis("localhost", 6379)

print(conn.keys("*"))

# Need to install redis server