import json
from datetime import datetime
import pytz
import sqlite3
import os
import re

DB_NAME = 'database.db'
DB_PATH = f"{DB_NAME}"


def now_time():  # Получение текущего времени по МСК
    now = datetime.now()
    tz = pytz.timezone('Europe/Moscow')
    now_moscow = now.astimezone(tz)
    current_time = now_moscow.strftime("%H:%M:%S")
    current_date = now_moscow.strftime("%Y.%m.%d")
    return current_date, current_time


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

def save_courses(data):
    for course, groups in data.items():
        if course == 'complex':
            continue
        for group_name, url in groups.items():
            SQL_request("""
                INSERT INTO groups (complex, name, url, course)
                VALUES (?, ?, ?, ?)
                ON CONFLICT(name) DO UPDATE SET
                    complex = excluded.complex,
                    url = excluded.url,
                    course = excluded.course
            """, (data['complex'], group_name, url, course))

import create_db