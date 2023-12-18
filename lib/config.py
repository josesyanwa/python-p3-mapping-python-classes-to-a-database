import sqlite3

DB_CONN= sqlite3.Connection("../db/music.db")
DB_CURSOR= DB_CONN.cursor()