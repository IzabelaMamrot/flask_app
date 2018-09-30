from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login'
#jesli uzytkownik nie jest zalogowany automatyczznie go przekieruje
#na strone logowania i po zalogowaniu przeniesie go na strone na ktorej byl
# Wartość 'login' powyżej to nazwa funkcji (lub punktu końcowego)
#  dla widoku logowania. Innymi słowy, nazwa, której użyjesz
# w url_for() aby uzyskać adres URL.

from app import routes, models