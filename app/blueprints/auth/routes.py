from . import auth_bp
from app.models import User
from app.extensions import db
from app.forms.auth import LoginForm, RegisterForm
from flask import jsonify, render_template, request, redirect, url_for
from flask_login import current_user, login_user, logout_user
from app.extensions import csrf

@auth_bp.route('/')
def auth():
    return render_template('auth/auth.html', login_form=LoginForm(), register_form=RegisterForm())

@auth_bp.route('/register', methods=['POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    
    print("=======form=====")
    print(request.form)
    
    registerform = RegisterForm(request.form)
       
    if registerform.validate_on_submit():
        username = registerform.username.data
        password = registerform.password.data
        
        user = User.query.filter_by(username=username).first()
        
        if not user:
            new_user = User(username=username)
            new_user.set_password(password)

            db.session.add(new_user)
            db.session.commit()

            login_user(new_user)
            next_page = request.args.get('next') or url_for('main.index')
            
            if request.headers.get('Accept') == 'application/json':
                return jsonify({
                    'message': 'User created',
                    'status' : 'ok',
                    'redirect': next_page
                }), 201
            return redirect(url_for('main.index'))
    
    return redirect(url_for('auth.auth'))


@auth_bp.route('/login', methods=['POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    
    loginform = LoginForm(request.form)
    
    if loginform.validate_on_submit():
        user = User.query.filter_by(username=loginform.username.data).first()
        
        if user and user.check_password(loginform.password.data):
            login_user(user)
            next_page = request.args.get('next') or url_for('main.index')
            
            if request.headers.get('Accept') == 'application/json':
                return jsonify({
                    'message': 'User logged in',
                    'status' : 'ok',
                    'redirect' : next_page
                })
            return redirect(next_page)
    
    return redirect(url_for('auth.auth'))


@auth_bp.route('/logout')
def logout():
    if current_user.is_authenticated:
        logout_user()
    
    return redirect(url_for('auth.auth'))