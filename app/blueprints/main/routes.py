from . import main_bp
from flask import render_template, redirect, url_for
from flask_login import login_required


@main_bp.route('/')
def index():
    return render_template('main/index.html')