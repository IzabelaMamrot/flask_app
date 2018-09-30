from datetime import datetime
from app import db, login
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin, db.Model): #klasa User dziedziczy po db.Model
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    def __repr__(self): #repejak printowac, przyda sie do debugowania
        return '<User {}>'.format(self.username)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    #timestamp zaindeksowane, co jest przydatne, jeśli
    # chcesz pobierać posty w porządku chronologicznym.
    #Zapewnia to używanie jednolitych znaczników czasu niezależnie od tego,
    # gdzie znajdują się użytkownicy.
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.body)


@login.user_loader #ladowanie danych - zamiana na int
def load_user(id):
    return User.query.get(int(id))


#Flask-Login śledzi zalogowanego użytkownika, przechowując jego
#unikalny identyfikator w sesji

#Alembic utrzymuje repozytorium migracji , które jest katalogiem,
# w którym przechowuje skrypty migracji. Za każdym razem,
# gdy wprowadzana jest zmiana w schemacie bazy danych,
#  do repozytorium dodawany jest skrypt migracji ze szczegółami zmiany.
# Aby zastosować migracje do bazy danych, te skrypty migracji są
# wykonywane w kolejności, w jakiej zostały utworzone.

#Aby automatycznie wygenerować migrację, Alembic porównuje schemat
# bazy danych zdefiniowany przez modele bazy danych z aktualnym
# schematem bazy danych. Następnie wypełnia skrypt migracji zmianami
# niezbędnymi do dostosowania schematu bazy danych do modeli aplikacji.