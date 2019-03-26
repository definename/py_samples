import redis
conn = redis.Redis()

sub = conn.pubsub()
sub.subscribe(["maine coon", "persian"])

for msg in sub.listen():
    if msg["type"] == "message":
        cat = msg["channel"].decode("utf-8")
        hat = msg["data"].decode("utf-8")
        print("Subscribe: {} wears a {}".format(cat, hat))