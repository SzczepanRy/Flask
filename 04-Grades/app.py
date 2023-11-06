# importowanie modułów i klas
from flask import Flask, render_template, session, redirect
from flask_bs4 import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
import json
from flask_moment import  Moment
from datetime import  datetime


# konfiguracja aplikacji
app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = 'bnhj^&*(IUGCH(*YT9uyhghji(*&YHJ' # klucz szyfrowania danych z formularza

moment = Moment(app)
date =datetime.now()

class LoginForm(FlaskForm):
    """
    Formularz logowania
    """
    userLogin = StringField('Nazwa użytkownika:', validators=[DataRequired()])
    userPass = PasswordField('Hasło:', validators=[DataRequired()])
    submit = SubmitField('Zaloguj')



# główna część aplikacji
@app.route('/')
def index():
    return render_template('index.html', title='Home')

@app.route('/logIn', methods=['POST', 'GET'])
def logIn():
    login = LoginForm()
    with open('data/users.json') as usersFile:
        users = json.load(usersFile)
        usersFile.close()
    if login.validate_on_submit():
        userLogin = login.userLogin.data
        userPass = login.userPass.data
        if userLogin == users['userLogin'] and userPass == users['userPass']:
            session['userLogin'] = userLogin
            session['firstName'] = users['firstName']
            return redirect('dashboard')
    return render_template('login.html', title='Logowanie', login=login)

@app.route('/logOut')
def logOut():
    session.pop('userLogin')
    return redirect('logIn')

@app.route('/dashboard')
def dashboard():
    with open("data/grades.json") as gradesfile:
        grades = json.load(gradesfile)
        gradesfile.close()
    return render_template('dashboard.html', title='Dashboard',grades=grades, userLogin=session.get('userLogin'),date=date, firstName=session.get('firstName'))

@app.errorhandler(404)
def pageNotFound(e):
    return render_template('404.html', title='nie ma takiej strony',userLogin=session.get('userLogin'), firstName=session.get('firstName')), 404

@app.errorhandler(500)
def serverError(e):
    return render_template('500.html', title="wewnętrzny błąd serwera", userLogin=session.get('userLogin'), firstName=session.get('firstName')), 500


# uruchomienie aplikacji
if __name__ == '__main__':
    app.run(debug=True)