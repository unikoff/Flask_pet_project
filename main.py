from flask import Flask, url_for, redirect, render_template, session, flash
from dotenv import load_dotenv

from flask_login import login_user, LoginManager, current_user, login_required, current_user, logout_user
from flask_login import current_user
from forms import*

from flask_sqlalchemy import SQLAlchemy
from database import Db_plus, random_active
from werkzeug.security import generate_password_hash, check_password_hash
app = Flask("__name__")
load_dotenv()
app.config.from_prefixed_env()

login_manager = LoginManager(app)
dbb = SQLAlchemy(app)


class UserModel(dbb.Model):
    __tablename__ = 'users'
    # we call our table in db / называем нашу таблицу в базе данных

    id = dbb.Column(dbb.Integer, primary_key=True)
    username = dbb.Column(dbb.String())
    email = dbb.Column(dbb.String(), unique=True)
    password = dbb.Column(dbb.String())


db = Db_plus(dbb, UserModel)


@login_manager.user_loader
def load_user(user):
    return db.find_id(user)


@app.route("/")
def index():
    return render_template("main.html")


@app.route('/profile/', methods=['POST', 'GET'])
@login_required
def profile():
    form = Profile()
    if form.validate_on_submit():
        if form.but_logout.data:
            logout_user()
            flash('Удачный выход', category='well')
            return redirect(url_for('login'))
        elif form.but_active.data:
            random_active_htm = random_active()
            return render_template('profile.html', form=form, random_active=random_active_htm)
    return render_template('profile.html', form=form)


@app.route('/login', methods=['POST', 'GET'])
def login():
    form = Log_in()
    if form.validate_on_submit():
        user = db.find_user(form.email.data)
        if not (user is None) and check_password_hash(user.get_psw(), form.password.data):
            login_user(user, remember=True)
            flash('Удачный вход', category='well')
            return redirect(url_for('profile'))
        else:
            flash('Что-то неверно', category='bad')
    return render_template('log_in.html', form=form)


@app.route('/registration', methods=['POST', 'GET'])
def registration():
    form = RegistrationForm()
    if form.validate_on_submit():
        if not db.exist_user(form.email.data):
            if db.new_user(username=form.username.data, email=form.email.data,
                               password=generate_password_hash(form.password.data)):
                user = db.find_user(form.email.data)
                login_user(user)
                flash('successful entry', category='well')
                return redirect(url_for('profile'))
        else:
            flash('user already exists', category='bad')
    return render_template("registration.html", form=form)


if __name__ == '__main__':
    app.run(debug=True)