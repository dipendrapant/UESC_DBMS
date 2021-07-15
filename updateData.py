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

# Update
try:
    dbCursor.execute("update student set name='Suvesh Khatri' where id = 3")
    db_conn.commit()

except:
    print("Update Error !")