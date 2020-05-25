import sqlite3

conn = sqlite3.connect('ppab6.db')
c = conn.cursor()

c.execute('''CREATE TABLE users
(
    username VARCHAR,
    password_hash VARCHAR
)
''')

conn.close()