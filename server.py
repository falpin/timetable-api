from flask import Flask, render_template, request, redirect, url_for, make_response, jsonify, flash, send_from_directory, jsonify
import sqlite3

app = Flask(__name__)

@app.route('/get_data', methods=['GET','POST'])
def receive_data():
    if request.method == 'POST':
        data = request.json # Получаем JSON-данные из запроса
        print(type(data))
        if not data: # Если данных нет
            return jsonify({"error": "Данные отстутсвуют"}), 400
        print(f"Полученные данные: {data}")
    
        # Ответ клиенту
        return jsonify({"message": "Данные успешно получены", "received_data": data}), 200
    elif request.method  == 'GET':
        return jsonify({"message": "Еу, эта страница для POST запросов"}), 200

@app.route("/", methods=['GET'])
def index():
    return jsonify({"message": "Эта главная страница, на которой не доступны POST запросы"})

app.run(host="0.0.0.0", port=5000)
# app.run()