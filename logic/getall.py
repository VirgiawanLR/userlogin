from connections.database.mysql import mydb


def getalldata():
    mycursor = mydb.cursor()
    sql = "SELECT * FROM masterdata"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    data_all = [{"id":item[0], "username":item[1], "email":item[3], "fullname":item[4]} for item in myresult]
    return data_all