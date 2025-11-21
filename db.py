import sqlite3
#https://docs.python.org/3/library/sqlite3.html

DB_FILE = "passwords.db"

con = sqlite3.connect(DB_FILE)
cur = con.cursor()
cur.execute("CREATE TABLE movie(title, year, score)")