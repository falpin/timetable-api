from scripts import *

if not os.path.exists(DB_PATH):
    SQL_request("""CREATE TABLE IF NOT EXISTS groups (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        complex TEXT,
        name TEXT UNIQUE,
        url TEXT,
        course TEXT,
        time_add TEXT DEFAULT CURRENT_TIMESTAMP,
        status TEXT DEFAULT "active"
    )""")
    print("База данных создана!")

def create_group(group):
    SQL_request(f"""CREATE TABLE IF NOT EXISTS {group} (
        week INTEGER UNIQUE,
        data JSON,
        time_add DATETIME DEFAULT CURRENT_TIMESTAMP
    )""")
    print(f"Группа {group} создана")