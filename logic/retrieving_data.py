
from connections.database.mysql import mydb
from connections.database.redis_con import redisClient


def retrieve_data(username,password):

    # redis checking

    from_redis = redisClient.hgetall(username)
    retrieve_from = ""
    data = {}
    if from_redis == {}:
        mycursor = mydb.cursor()

        sql = "SELECT * FROM masterdata WHERE username=%s and `password`=%s"
        val = (username, password)
        mycursor.execute(sql, val)
        myresult = mycursor.fetchall()
        if myresult == []:
            return False, retrieve_from, data
        else:
            myresult = myresult[0]
            redisClient.hset(username, 'password', password)
            print("--------------------------------", myresult)
            redisClient.hset(username, 'email', myresult[3])
            redisClient.hset(username, 'fullname', myresult[4])
            redisClient.expire(name=username, time=20)
            data = {
                "username": username,
                "fullname": myresult[4],
                "email": myresult[3]
            }
            retrieve_from = "DB"
            return True, retrieve_from, data
    else:
        if from_redis['password'] == password:
            retrieve_from = "Redis"
            data = {
                "username": username,
                "fullname": from_redis['fullname'],
                "email": from_redis['email']
            }
            return True, retrieve_from, data
        else:
            return False, retrieve_from, data
