import sqlite3
import os


MY_DB = 'ppab6.db'


def check_if_db_exists():
    if os.path.isfile(MY_DB):
        recreate = input(
            f'{MY_DB} exists. Would you like to delete and recreate it? (y or n) '
            )
        if recreate == 'y':
            os.remove(MY_DB)
            create_db()
            return 'Database recreated'
        elif recreate == 'n':
            return 'Not recreating the database'
        else:
            return 'Invalid answer. Please answer y or n.'
    else:
        create_db()


def create_db():
        conn = sqlite3.connect(MY_DB)
        c = conn.cursor()

        c.execute('''CREATE TABLE users
        (
            username VARCHAR,
            password_hash VARCHAR
        )
        ''')

        conn.close()

