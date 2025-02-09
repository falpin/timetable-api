import sqlite3

DB_NAME = 'database.db'
DB_PATH = f"{DB_NAME}"

def SQL_request(request, params=(), all_data=None):  # Выполнение SQL-запросов
    connect = sqlite3.connect(DB_PATH)
    cursor = connect.cursor()
    if request.strip().lower().startswith('select'):
        cursor.execute(request, params)
        if all_data == None: result = cursor.fetchone()
        else: result = cursor.fetchall()
        connect.close()
        return result
    else:
        cursor.execute(request, params)
        connect.commit()
        connect.close()

def create_groups():
    SQL_request("""CREATE TABLE IF NOT EXISTS groups (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        complex TEXT,
        group_name TEXT UNIQUE,
        url TEXT,
        course TEXT,
        time_add TEXT DEFAULT CURRENT_TIMESTAMP,
        status TEXT DEFAULT "active"
    )""")

def create_group(group):
    SQL_request(f"""CREATE TABLE IF NOT EXISTS {group} (
        week INTEGER UNIQUE,
        data JSON,
        time_add DATETIME DEFAULT CURRENT_TIMESTAMP
    )""")
    print(f"Группа {group} создана")

create_groups()