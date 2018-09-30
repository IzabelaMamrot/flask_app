from flask import render_template, flash, redirect
from flask_login import current_user, login_user, logout_user
from app import app
from app.forms import LoginForm
from app.models import User

@app.route('/') #dokoratory tworzine miedzy URL a argumentem funkcji
@app.route('/index')
def index():
    user = {'username': 'Wojtasek '} #slownik- json

    return render_template('index.html', title='First Page', user=user)
    #''' bedzie zwocone wszytko co jest w '''
#Mamy dwa dekoratory, oznacza to ze przegladarka zazada jeden z dwoch adresow URL, a flask wywola te funkcje i przekaze jej wartosc


@app.route('/login', methods=['GET', 'POST']) #metody sa w dekoratorze mowi to o tym jaki widok moze uzyc zadan GET-info od klienta, POST do formularzy
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))
    return render_template('login.html', title='Sing In', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

