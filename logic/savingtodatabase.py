
from connections.database.mysql import mydb


def save_data(userdict):

    mycursor = mydb.cursor()

    sql = "INSERT INTO masterdata (username, `password`, email, fullname) VALUES (%s, %s, %s, %s)"
    val = (userdict.username, userdict.password, userdict.email, userdict.fullname)

    try:
        mycursor.execute(sql, val)
        mydb.commit()
    except:
        return False
    # print(mycursor.rowcount, "record inserted.")
    # print(mydb)
    return True
