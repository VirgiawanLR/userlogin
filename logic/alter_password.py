
from connections.database.mysql import mydb



def retrieve_data(username,password):

    mycursor = mydb.cursor()

    sql = "SELECT username, `password` FROM masterdata WHERE username=%s and `password`=%s"
    val = (username, password)
    mycursor.execute(sql, val)

    myresult = mycursor.fetchall()
    
    if myresult == []:
        return False
    else:
        return True

def altering(username, password_change):

    mycursor = mydb.cursor()

    sql = "UPDATE masterdata SET `password`=%s WHERE username=%s "
    val = (password_change, username)
    mycursor.execute(sql, val)
    myresyult = mycursor.fetchall
    print(myresyult)
    mydb.commit()
    return True