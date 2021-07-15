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

# Delete
try:
    dbCursor.execute("delete from student where id = 3")
    db_conn.commit()

except:
    print("Deleteion Error !")