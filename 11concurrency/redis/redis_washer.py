import redis
conn = redis.Redis()

print("Washer is being started...")

# We need to clean up dishes list in case if it is not empty.
conn.delete("dishes")

dishes = ["salad", "bread", "entee", "dessert"]

# push dishes into the redis.
for index, dish in enumerate(dishes):
    msg = dish.encode("utf-8")
    conn.rpush("dishes", msg)
    print("Washed {}".format(index))

conn.rpush("dishes", "quit")
print("Washer is done")