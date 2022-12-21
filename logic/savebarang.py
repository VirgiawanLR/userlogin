from connections.database.mysql import mydb


def save_barang(userdict):

    mycursor = mydb.cursor()

    sql = "INSERT INTO barang (namabarang, harga, personid, sertifikatid) VALUES (%s, %s, %s, %s)"
    val = (userdict.namabarang, userdict.harga, userdict.personid, userdict.sertifikatid)

    try:
        mycursor.execute(sql, val)
        mydb.commit()
    except:
        return False

    return True