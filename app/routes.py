from flask import render_template, flash, url_for, redirect, request
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.urls import url_parse
from app import app, ups
from app.forms import LoginForm
from app.models import User

summary = "UPS: {}, {}".format(ups.description(app.config['NUT_UPS_NAME']), ups.ver())

@app.route('/')
@app.route('/index')
@app.route('/status')
def status():
    ups_vars = ups.list_vars(app.config['NUT_UPS_NAME'])
    return render_template('status.html', title='UPS Status', summary=summary, ups_vars=ups_vars)

@app.route('/commands')
@login_required
def commands():
    ups_commands = ups.list_commands(app.config['NUT_UPS_NAME'])
    return render_template('commands.html', title='UPS Commands', summary=summary, ups_commands=ups_commands)

@app.route('/settings')
@login_required
def settings():
    ups_settings = ups.list_rw_vars(app.config['NUT_UPS_NAME'])
    return render_template('settings.html', title='UPS Settings', summary=summary, ups_settings=ups_settings)

@app.route('/server')
@login_required
def server():
    return redirect(url_for('status'))

@app.route('/appconfig')
@login_required
def appconfig():
    return redirect(url_for('status'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('status'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('status')
        return redirect(next_page)
    return render_template('login.html', form=form, title="Log In")

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('status'))