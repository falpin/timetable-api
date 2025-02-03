from flask import Flask, jsonify, Blueprint
import sqlite3

Blueprint = Blueprint(
    "api",
    __name__,
    template_folder='templates',
    static_folder='static',
    url_prefix='/api'
)

@Blueprint.route('/', methods=['GET'])
def example():
    return jsonify({"message": "API Работает"}), 200


if __name__ == '__main__':
    app = Flask(__name__)
    app.register_blueprint(Blueprint)
    app.run( host='0.0.0.0', port=80, debug=True)