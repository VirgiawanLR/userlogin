import redis
import os
from dotenv import load_dotenv


# dotenv_path = Path('/home/virgiawan/project/User_SignUp_SignIn/.env')
# load_dotenv(dotenv_path=dotenv_path)

load_dotenv()


redisClient = redis.StrictRedis(
    host=os.getenv('REDIS_HOST'), 
    port=6379, 
    db=0, 
    charset="utf-8", 
    decode_responses=True
    )


# Add key value pairs to the Redis hash

# hashName = "Dessert"

# redisClient.hset(hashName, 1, "Cheesecake")

# redisClient.hset(hashName, 2, "Apple Pie")

# # Print the hash

# print(redisClient.hgetall(hashName))



# # Remove a key

# redisClient.hdel(hashName, 1)

 

# # Print the hash after removing a key

# print(redisClient.hgetall(hashName))

# print(redisClient.hgetall("capitals"))
# # import redis


# foo = {
#     "installation_type": "esxi",
#     "host_short_name": "esxi021"
# }

# redis_connection = redis.StrictRedis(host='localhost', port=6379, charset="utf-8", decode_responses=True)
# redis_connection.hset("test", mapping=foo)
# print(redis_connection.hgetall("test"))


# pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
# redis2 = redis.Redis(connection_pool=pool)
# redis1 = redis.StrictRedis(connection_pool=pool, charset="utf-8", decode_responses=True)
# redis1.set('mykey', 'Hello from Python!')
# value = redis1.get('mykey').decode('utf-8')
# print(value)

# redis1.zadd('vehicles', {'car' : 0})
# redis1.zadd('vehicles', {'bike' : 0})
# vehicles = redis1.zrange('vehicles', 0, -1)
# for item in vehicles:
#     print(item.decode('utf-8'))
# print(vehicles)


# redis1.lpush('foo', *[1,2,3,4,5,6,7,8,9])
# print(redis1.lrange('foo', 0, -1))
# # redis1.hset({"Croatia": "Zagreb", "Bahamas": "Nassau"})
# # capital = redis1.mget("Croatia", "Bahamas")
# # print(capital)

# import the Redis client

# import redis

 

# Create a redis client

                               

