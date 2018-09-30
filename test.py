from app import app, db
from app.models import User, Post

@app.shell_context_processor #jawne zaimplementowanie przydaje sie do sprawzdenia w sheluu
#usuchamiamy shella - flask shell
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}

#from app import app

#plik do zdefiniowwania instancji aplikacji. Instrukcja app import app
# importuje zmienną aplikacji, która jest członkiem pakietu aplikacji
