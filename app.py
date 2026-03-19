from flask import Flask, request, jsonify, send_from_directory
import os

HERE = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__, static_folder=HERE, template_folder=HERE)

@app.route('/')
def index():
    return send_from_directory(HERE, 'index.html')

@app.route('/dashboard')
def dashboard():
    return send_from_directory(HERE, 'dashboard.html')

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json() or {}
    username = data.get('username')
    password = data.get('password')
    if username == 'admin' and password == 'secret':
        return jsonify({'success': True})
    return jsonify({'success': False, 'message': 'Credenciais inválidas'}), 401

if __name__ == '__main__':
    app.run(debug=True)
