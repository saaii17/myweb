from flask import Blueprint, render_template, request, jsonify
from pymongo import MongoClient
from werkzeug.security import generate_password_hash, check_password_hash

auth_bp = Blueprint('auth', __name__)

# MongoDB connection setup
client = MongoClient("mongodb://localhost:27017/")
db = client["event_db"]
users_collection = db["users"]

# Login/Signup page
@auth_bp.route('/')
def login_page():
    return render_template('login.html')

# Signup endpoint
@auth_bp.route('/auth/signup', methods=['POST'])
def signup():
    data = request.get_json()
    email = data.get('email')
    name = data.get('name')
    password = data.get('password')

    if users_collection.find_one({'email': email}):
        return jsonify({'success': False, 'message': 'User already exists'})

    hashed_pw = generate_password_hash(password)
    users_collection.insert_one({
        'name': name,
        'email': email,
        'password': hashed_pw
    })

    return jsonify({'success': True, 'message': 'Signup successful'})

# Login endpoint
@auth_bp.route('/auth/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    user = users_collection.find_one({'email': email})
    if user and check_password_hash(user['password'], password):
        return jsonify({'success': True, 'message': 'Login successful'})
    return jsonify({'success': False, 'message': 'Invalid credentials'})

# Vendor page
@auth_bp.route('/vendor')
def vendor():
    return render_template('vendor.html')

@auth_bp.route('/catering')
def catering():
    return render_template('catering.html')

# Individual service pages
@auth_bp.route('/marrageg')
def marrageg():
    return render_template('marrageg.html')

@auth_bp.route('/birthday')
def birthday():
    return render_template('birthday.html')

@auth_bp.route('/corporate')
def corporate():
    return render_template('corporate.html')

@auth_bp.route('/engment')
def engment():
    return render_template('engment.html')

@auth_bp.route('/festival')
def festival():
    return render_template('festival.html')

@auth_bp.route('/chatbot')
def chatbot():
    return render_template('chatbot.html')

@auth_bp.route('/naming')
def naming():
    return render_template('naming.html')

@auth_bp.route('/haldihmendi')
def haldihmendi():
    return render_template('Haldimhendi.html')

@auth_bp.route('/freshers')
def freshers():
    return render_template('birthday.html')  # Reusing birthday template
