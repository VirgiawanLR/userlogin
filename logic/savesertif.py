from connections.database.mysql import mydb


def save_sertif(userdict):

    mycursor = mydb.cursor()

    sql = "INSERT INTO sertifikat (personid) VALUES (%s)"
    val = (userdict.personid,)

    try:
        mycursor.execute(sql, val)
        mydb.commit()
    except:
        return False

    return True