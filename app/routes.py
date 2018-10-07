from flask import render_template, flash, redirect, request
from flask_login import current_user, login_user, logout_user, login_required
from app import app, db
from app.forms import LoginForm, RegistrationForm
from app.models import User
from werkzeug.urls import url_parse

@app.route('/') #dokoratory tworzine miedzy URL a argumentem funkcji
@app.route('/index')
#@login_required
def index():
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='First Page', posts=posts)
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
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sing In', form=form)
#Jeśli adres URL logowania nie ma next argumentu, użytkownik jest
# przekierowywany na stronę indeksu.
#Jeśli adres URL logowania zawiera next argument, który jest ustawiony
#na inna sciezke, wówczas
# użytkownik jest przekierowywany do tego adresu URL.
#Jeśli adres URL logowania zawiera next argument, który jest ustawiony
#  na pełny adres URL, który zawiera nazwę domeny, wówczas użytkownik
# jest przekierowywany na stronę indeksu.


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated: #czy nie jest zalogowany
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit(): #obsluga formularza - tworzenie nowego uzytkownika
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

