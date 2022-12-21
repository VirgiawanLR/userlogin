from connections.database.mysql import mydb


def check(dict):

    mycursor = mydb.cursor()
    
    sql = "SELECT sertifikatid FROM barang WHERE barangid = %s"
    val = (dict.barangid,)
    mycursor.execute(sql,val)
    myresult = mycursor.fetchall()
    if len(myresult) == 0:
        return "False"

    if myresult[0][0] is None:
        return "Imitation"
    else:
        return "Original"