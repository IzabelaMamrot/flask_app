import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-neer-guess'
    # pobieranie bazych danych
    #jesli baza nie jest zefiniowana konfiguruje baze app.db
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    #zmiany w bazie, domysle na False
    SQLALCHEMY_TRACK_MODIFICATIONS = False