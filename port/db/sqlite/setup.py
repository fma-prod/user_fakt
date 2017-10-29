import sqlite3

from config import DB_NAME

conn = sqlite3.connect(DB_NAME)


def create_tables():
    cursor = conn.cursor()
    cursor.execute("""
      CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
        name TEXT,
        age INTERGER
        )
        """)


def remove_table(table):
    cursor = conn.cursor()
    cursor.execute("""
      DROP TABLE {table_name}
      """.format(table_name=table))