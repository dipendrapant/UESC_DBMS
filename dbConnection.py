import mysql.connector

# create a connection string
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
