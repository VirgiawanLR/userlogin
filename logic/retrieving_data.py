
from connections.database.mysql import mydb



def retrieve_data(username,password):

    mycursor = mydb.cursor()

    sql = "SELECT username, `password` FROM masterdata WHERE username=%s and `password`=%s"
    val = (username, password)
    mycursor.execute(sql, val)

    myresult = mycursor.fetchall()
    print(myresult)
    if myresult == []:
        return False
    else:
        return True
