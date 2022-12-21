from connections.database.mysql import mydb


def getalldata():
    mycursor = mydb.cursor()
    sql = "SELECT * FROM barang"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    print(myresult)
    data_all = [{"barangid":item[0], "namabarang":item[1], "ownerid":item[3], "harga":item[2], "sertifikatid":item[4]} for item in myresult]
    return data_all