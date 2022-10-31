import sqlite3 as sql

#connect to SQLite
con = sql.connect('db_web.db')

#Create a Connection
cur = con.cursor()

#Drop users table if already exsist.
cur.execute("DROP TABLE IF EXISTS users")

#Create users table  in db_web database
sql =''''CREATE TABLE "users" (
	"UNAME"	INTEGER PRIMARY KEY AUTOINCREMENT,
	"NAME"	TEXT,
	"CONTACT" NUMBER,
	"EMAIL" MAIL
)''''
cur.execute(sql)

#commit changes
con.commit()

#close the connection
con.close()