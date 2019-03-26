import zmq

ctx = zmq.Context()
sub = ctx.socket(zmq.SUB)
sub.connect("tcp://{}:{}".format("127.0.0.1", 6789))

# set socket options
topics = ["maine coon", "persian"]
for topic in topics:
    sub.setsockopt(zmq.SUBSCRIBE, topic.encode("utf-8"))

# receive multipart message
while True:
    cat_bytes, hat_bytes = sub.recv_multipart()
    cat = cat_bytes.decode("utf-8")
    hat = hat_bytes.decode("utf-8")
    print("Subscribe: {} wears: {}".format(cat, hat))