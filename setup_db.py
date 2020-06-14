import sqlite3
import os


MY_DB = 'ppab6.db'


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


def check_db():
        conn = sqlite3.connect(MY_DB)
        c = conn.cursor()
        c.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = c.fetchall()

        print(f'\n{MY_DB} exists.')
        print(f'The tables currently in {MY_DB} are {tables}.')

        for table in tables:
            tbl_name = table[0]
            c.execute(f"SELECT count(*) FROM {tbl_name}")
            print(f'\n{tbl_name} has {c.fetchone()[0]} rows.')

        conn.close()


def check_if_db_exists():
    if os.path.isfile(MY_DB):
        check_db()
        recreate = input(
            f'\nWould you like to delete and recreate it? (y or n) '
            )
        if recreate == 'y':
            os.remove(MY_DB)
            create_db()
            return 'Database recreated.'
        elif recreate == 'n':
            return 'Not recreating the database. Exiting.'
        else:
            return 'Invalid answer. Please answer y or n.'
    else:
        create_db()


if __name__ == "__main__":
    print(check_if_db_exists())