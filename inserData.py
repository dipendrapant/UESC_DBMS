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

#cursor
dbCursor = db_conn.cursor()

try:
    dbCursor.execute("insert into student (id,name,phone) values (3,'Suvesh','98456')")
    db_conn.commit()

except:
    print("Insert Error !")