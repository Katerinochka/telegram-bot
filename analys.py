from db import *

def get_data():
    conn = get_connection()
    c = conn.cursor()
    c.execute('SELECT * FROM user_message')
    res = c.fetchall()
    return res

print(get_data())