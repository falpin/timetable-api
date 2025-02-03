from scripts import *

if not os.path.exists(DB_PATH):
    SQL_request("""CREATE TABLE IF NOT EXISTS groups (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        complex TEXT,
        name TEXT UNIQUE,
        url INTEGER,
        course TEXT,
        time_add DATETIME DEFAULT CURRENT_TIMESTAMP,
        status TEXT DEFAULT "active"
    )""")
    print("База данных создана!")