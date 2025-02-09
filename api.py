from flask import Flask, jsonify, Blueprint, request, abort
import config
from scripts import *

Blueprint = Blueprint(
    "api",
    __name__,
    template_folder='templates',
    static_folder='static',
    url_prefix='/api'
)

ALLOWED_API_KEYS = config.API_KEYS

def check_api_key(api_key):
    if api_key not in ALLOWED_API_KEYS:
        abort(401, description="Неверный API ключ")  # Возвращает 401 Unauthorized если ключ недействителен

def save_data(function, request):
    try:
        api_key = request.headers.get('X-API-Key')
        check_api_key(api_key)
        
        data = request.get_json()
        if not data:
            return ({"error": "Пустой запрос"}), 400
        function(data)        
        return ("Сохранено!"), 200
    
    except Exception as e:
        return ({"error": f"Произошла ошибка: {str(e)}"}), 500


@Blueprint.route('/', methods=['GET'])
def example():
    return jsonify({"message": "API Работает"}), 200

@Blueprint.route('save_groups', methods=['POST'])
def saving_groups():
    text, code = save_data(save_groups, request)
    return jsonify(text), code

@Blueprint.route('/save_schedule', methods=['POST'])
def saving_schedule():
    text, code = save_data(save_schedule, request)
    return jsonify(text), code

@Blueprint.route('get_groups', methods=['GET', 'POST'])
def get_groups():
    if request.method == "GET":
        group = None
    elif request.method == "POST":
        data = request.get_json()
        group = data['group']
    groups, code = find_groups(group)
    return jsonify(groups), code


if __name__ == '__main__':
    app = Flask(__name__)
    app.register_blueprint(Blueprint)
    app.run(port=80, debug=True)