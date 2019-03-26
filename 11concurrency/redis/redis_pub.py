import redis
import random
conn = redis.Redis()

cats = ["siamese", "persian", "maine coon", "norwegian forest"]
hats = ["stovepipe", "bowler", "tam-o-shanter", "fedora"]

for msg in range(10):
    cat = random.choice(cats)
    hat = random.choice(hats)
    print("Publish: {} wears a {}".format(cat, hat))
    conn.publish(cat, hat)