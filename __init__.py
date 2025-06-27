from flask import Flask
from .db import users_collection  # Just to ensure db is initialized
from .auth import auth_bp
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    app.secret_key = 'super_secret_key'
    CORS(app)

    # Register Blueprint
    app.register_blueprint(auth_bp)

    # Root route
    @app.route('/')
    def index():
        return app.send_static_file('login.html')  # Or: render_template('login.html')

    @app.route('/vendor')
    def vendor():
        from flask import session, render_template, redirect
        if 'email' in session:
            return render_template('vendor.html')
        return redirect('/')

    return app
