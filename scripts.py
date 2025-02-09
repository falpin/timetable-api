import json
from datetime import datetime
import pytz
import os
import re
from use_db import *


def now_time():  # Получение текущего времени по МСК
    now = datetime.now()
    tz = pytz.timezone('Europe/Moscow')
    now_moscow = now.astimezone(tz)
    current_time = now_moscow.strftime("%H:%M:%S")
    current_date = now_moscow.strftime("%Y.%m.%d")
    return current_date, current_time

def save_groups(data):
    for course, groups in data.items():
        if course == 'complex':
            continue
        for group_name, url in groups.items():
            date, time = now_time()  # Обновляем время для каждой группы
            timestamp = f"{date} {time}"
            SQL_request("""
                INSERT INTO groups (complex, group_name, url, course, time_add)
                VALUES (?, ?, ?, ?, ?)
                ON CONFLICT(group_name) DO UPDATE SET
                    complex = excluded.complex,
                    url = excluded.url,
                    course = excluded.course,
                    time_add = excluded.time_add  -- Обновляем время добавления
            """, (data['complex'], group_name, url, course, timestamp))

def save_schedule(data):
    week = data["week"]
    group = data["group"]
    new_data = data.copy()
    del new_data["week"]
    del new_data["group"]
    group = group.replace("-", "_")
    create_group(group)
    data = new_data
    date, time = now_time()  # Обновляем время для каждой группы
    timestamp = f"{date} {time}"
    SQL_request(f"""
        INSERT INTO {group} (week, data, time_add)
        VALUES (?, ?, ?)
        ON CONFLICT(week) DO UPDATE SET
            week = excluded.week,
            time_add = excluded.time_add
    """, (week, json.dumps(data), timestamp))


def find_groups(find_group=None):
    groups = SQL_request("SELECT * FROM groups", all_data=True)
    if groups:
        groups_list = {}
        for group in groups:
            group_dict = {
                "id": group[0],
                "complex": group[1],
                "url": group[3],
                "course": group[4]
            }
            groups_list[group[2]] = (group_dict)
        try:
            if find_group:
                groups_list = groups_list[find_group]
        except:
            return "Группа не найдена", 400
        groups_json = json.dumps(groups_list, indent=4, ensure_ascii=False)
        return groups_json, 200
    else:
        return None, 400