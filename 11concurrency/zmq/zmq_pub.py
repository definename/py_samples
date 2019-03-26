import zmq
import random
import time

ctx = zmq.Context()
pub = ctx.socket(zmq.PUB)
pub.bind("tcp://{}:{}".format("*", 6789))

cats = ["siamese", "persian", "maine coon", "norwegian forest"]
hats = ["stovepipe", "bowler", "tam-o-shanter", "fedora"]

time.sleep(1)

for msg in range(10):
    cat = random.choice(cats)
    cat_bytes = cat.encode("utf-8")

    hat = random.choice(hats)
    hat_bytes = hat.encode("utf-8")

    print("Publish: {} wears: {}".format(cat, hat))
    pub.send_multipart([cat_bytes, hat_bytes])