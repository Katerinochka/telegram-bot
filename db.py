import sqlite3
import datetime

__connection = None
def get_connection():
    global __connection
    if __connection is None:
        __connection = sqlite3.connect('anketa.db', check_same_thread=False)
    return __connection

def init_db(force: bool = False):
    conn = get_connection()

    c = conn.cursor()
    # Сообщения от пользователей
    if force:
        c.execute('DROP TABLE IF EXISTS user_message')

    c.execute('''
        CREATE TABLE IF NOT EXISTS user_message (
            id          INTEGER PRIMARY KEY,
            user_id     INTEGER NOT NULL,
            level_id    INTEGER,
            datetime    DATETIME NOT NULL 
        )
    ''')

    conn.commit()

def add_message(user_id, level_id):
    conn = get_connection()
    c = conn.cursor()
    date_time = datetime.datetime.now()
    c.execute('INSERT INTO user_message (user_id, level_id, datetime) VALUES (?,?,?)', (user_id,level_id, date_time))

    conn.commit()
