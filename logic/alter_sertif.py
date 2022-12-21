from connections.database.mysql import mydb


def alter_sertif(dict):

    mycursor = mydb.cursor()
    
    sql = "SELECT * FROM barang WHERE barangid = %s"
    val = (dict.barangid,)
    mycursor.execute(sql,val)
    myresult = mycursor.fetchall()
    if len(myresult) == 0:
        return False


    sertifid = myresult[0][4]
    if sertifid is None:

        sql = "UPDATE barang SET sertifikatid = %s WHERE barangid = %s "
        val = (dict.sertifikatid, dict.barangid)


        mycursor.execute(sql, val)
        mydb.commit()
    
        return True
    else:
        return False