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

@Blueprint.route('/', methods=['GET'])
def example():
    return jsonify({"message": "API Работает"}), 200

@Blueprint.route('/get_groups', methods=['POST'])
def get_groups():
    try:
        api_key = request.headers.get('X-API-Key')
        check_api_key(api_key)
        
        data = request.get_json()
        if not data:
            return jsonify({"error": "Пустой запрос"}), 400
        save_courses(data)
        return jsonify("Успешно!"), 200
    
    except Exception as e:
        return jsonify({"error": f"Произошла ошибка: {str(e)}"}), 500


if __name__ == '__main__':
    app = Flask(__name__)
    app.register_blueprint(Blueprint)
    app.run(port=80, debug=True)