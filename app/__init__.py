from flask_login import login_required
from app.models import User
from app.blueprints import auth_bp, main_bp
from flask import Flask, jsonify, render_template, url_for
from .extensions import db, login_manager, migrate, csrf
from flask_wtf.csrf import generate_csrf


def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    
    db.init_app(app)
    migrate.init_app(app,db)
    login_manager.init_app(app)
    csrf.init_app(app)
    login_manager.login_view = 'auth.auth'
    
    with app.app_context():
        from flask_migrate import upgrade
        upgrade()
    
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(main_bp, url_prefix='/main')
    
    @app.route('/api/csrf-token', methods=['GET'])
    def csrf_token():
        token = generate_csrf()
        return jsonify({'csrf_token': token})
    
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    @app.route('/')
    @login_required
    def index():
        return render_template('home.html')
    
    @app.route("/site-map")
    def site_map():
        links = []
        for rule in app.url_map.iter_rules():
            # Filter out rules we can't navigate to in a browser
            # and rules that require parameters
            if "GET" in rule.methods and has_no_empty_params(rule):
                url = url_for(rule.endpoint, **(rule.defaults or {}))
                links.append((url, rule.endpoint))
        return '<br>'.join(['<a href="{url}">{endpoint}</a>'.format(url=url, endpoint=endpoint) for url, endpoint in links])
    
    
    return app

def has_no_empty_params(rule):
    defaults = rule.defaults if rule.defaults is not None else ()
    arguments = rule.arguments if rule.arguments is not None else ()
    return len(defaults) >= len(arguments)
