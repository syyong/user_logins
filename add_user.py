import sqlite3
import hashlib

from setup_db import check_db

MY_DB = 'ppab6.db'


def check_user_exists(cur, name):
    query = f"select * from users where username = '{name}'"
    print(query)
    cur.execute(query)
    if cur.fetchone():
        return True
    return False 

def check_insert(cur):
    cur.execute("SELECT * FROM users;") 
    rows = cur.fetchall()
    for i in rows:
        print(i)


def add_user():
    name = input("Please enter your name: ")
    conn = sqlite3.connect(MY_DB)

    try:
        with conn:
            cur = conn.cursor()
            while True:
                user_exists = check_user_exists(cur, name)
                if user_exists:
                    name = input('This username is taken. Please enter a new one: ')
                else:
                    password = input("Please enter your password: ")
                    password_hash = hashlib.sha256(password.encode('utf-8')).hexdigest()
                    conn.execute(
                        f"""INSERT INTO users (username, password_hash)
                        VALUES ('{name}', '{password_hash}');"""
                    )
                    check_insert(cur)
                    break
    except sqlite3.IntegrityError:
        print(f"couldn't add {name} twice.")


def return_user():
    name = input("Please enter your name: ")
    return name

if __name__ == "__main__":
    add_user()
