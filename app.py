from flask import Flask, render_template, request, redirect, jsonify
from flask_cors import CORS
import os
from flask import Flask
from auth import auth_bp


app = Flask(__name__)
CORS(app)  # Allows JS fetch() to work smoothly
app.register_blueprint(auth_bp)

# Dummy database (use MongoDB/SQLite in real app)
users = []

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/auth/signup', methods=['POST'])
def signup():
    data = request.get_json()
    email = data['email']
    if any(u['email'] == email for u in users):
        return jsonify({'success': False, 'message': 'User already exists!'})
    users.append(data)
    return jsonify({'success': True, 'message': 'Signup successful!'})

@app.route('/auth/login', methods=['POST'])
def login():
    data = request.get_json()
    for u in users:
        if u['email'] == data['email'] and u['password'] == data['password']:
            return jsonify({'success': True, 'message': 'Login successful!'})
    return jsonify({'success': False, 'message': 'Invalid credentials'})

@app.route('/')
def home():
    return render_template('vendor.html')

if __name__ == '__main__':
    app.run(debug=True)
