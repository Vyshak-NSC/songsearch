from . import main_bp
from flask import render_template, redirect, url_for
from flask_login import login_required


@main_bp.route('/')
@login_required
def index():
    return render_template('main/index.html')

@main_bp.route('/search')
@login_required
def search():
    return render_template('main/search.html')