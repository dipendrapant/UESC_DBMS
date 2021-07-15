import mysql.connector
db_conn = mysql.connector.connect(
     host = "localhost",
    user = "admin",
    password = "",
    database = "becomputerDB"
)


if (db_conn):
    print("Database Connected Successfully !")

else:
    print("Database Conncetion Unsuccessful !")

dbCursor = db_conn.cursor()

try:
    dbCursor.execute("select * from student")
    for i in dbCursor:
        print(i)

except:
    print("Data View Error !")