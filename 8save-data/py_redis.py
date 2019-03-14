# Need to to install WSL and Redis server

import redis
conn = redis.Redis("localhost", 6379)

# lists all available keys
print(conn.keys("*"), end="\n\n")

## strings

keys = ["secret", "carats", "fever"]
print("keys were removed: {}".format(conn.delete(*keys)))

    # set key
for index, key in enumerate(keys):
    print("key: {} was set: {}".format(key, conn.set(key, index)))

    # get key
getkeys = """secret is: {}
carats is: {}
fever is: {}""".format(conn.get("secret"), conn.get("carats"), conn.get("fever"))

print(getkeys)

    # replace
print("'secret' key old value: {} was replaced with new one".format(conn.getset("secret", "newsecretvalue")))

    # delete
print("'fever' key was deleted: {}".format(conn.delete("fever")), end="\n\n")

## lists

print("'zoolist' was deleted: {}".format(conn.delete("zoolist")))
zoolist = ["tiger", "parrot"]
    # push
print("'zoolist' variable was pushed into the list: {}".format(conn.lpush("zoolist", *zoolist)))

    # length
print("'zoolist' list legth is: {}".format(conn.llen("zoolist")))

    # get range
print("'zoolist' list contains: {}".format(conn.lrange("zoolist", 0, -1)), end="\n\n")

## hash aka dict

    # delete
print("'songdict' was deleted: {}".format(conn.delete("songdict")))

    # set
songdict = {
    "do": "a deer",
    "re": "about a deer"
}
print("'songdict' hash was set: {}".format(conn.hmset("songdict", songdict)))

    # get
print("'songdict' hash value: {}".format(conn.hmget("songdict", songdict.keys())), end="\n\n")

## set

    # delete
print("'zooset' was deleted: {}".format(conn.delete("zooset")))

    # set
zooset = { "duck", "goat", "turkey" }
print("'zooset' set value: {}".format(conn.sadd("zooset", *zooset)))

    # length
print("'zooset' lenght: {}".format(conn.scard("zooset")))

    # get
print("'zooset' lenght: {}".format(conn.smembers("zooset")))
