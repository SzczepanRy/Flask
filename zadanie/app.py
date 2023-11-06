#import modulow i klas
# importowanie modułów i klas
from flask import Flask, render_template, session, redirect
from flask_bs4 import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
import math


#konfig app
app = Flask(__name__)
bootstrap = Bootstrap(app)

class LoginForm(FlaskForm):
    """
    Formularz logowania
    """
    a = StringField('Podaj A:', validators=[DataRequired()])
    b = StringField('Podaj B:', validators=[DataRequired()])
    c = StringField('Podaj C:', validators=[DataRequired()])

users = {
    'userLogin': 'aslusarczyk',
    'userPass': 'Qwerty123!',
    'firstName': 'Adam',
    'lastName': 'Ślusarczyk'
}

#glowna czesc app

@app.route('/')
def index():
    return render_template('index.html', title='Home')

@app.route('/logIn', methods=['POST', 'GET'])
def logIn():
    login = LoginForm()
    if login.validate_on_submit():
        # userLogin = login.userLogin.data
        # userPass = login.userPass.data
        # if userLogin == users['userLogin'] and userPass == users['userPass']:
        #     session['userLogin'] = userLogin
        #     return redirect('dashboard')
        a = float(login.A.data)
        b = float(login.B.data)
        c = float(login.C.data)
        print(a,b,c)
        session['a'] = a
        session['b'] = b
        session['c'] = c

        #if a(!= 0):
        delta = (b ** 2) - (4*a*c)
        session["delta"] = delta
        if delta > 0:
            x1 = (-b -math.sqrt(delta)) / (a*2)
            x2 = (-b - math.sqrt(delta)) / (a * 2)
            session["x1"] = round(x1,2)
            session['x2'] = round(x2,2)
            print('x1 = '), x1, ('x2 = '), x2
        elif delta == 0:
            x1 = -b /(2*a)
            x2 = "brak"
            session ['x1'] = round(x1,2)
            session ['x2'] = x2
            print("x = "), x1
        else:
            x1 = "brak"
            x2 = "brak"
            session['x1'] = x1
            session['x2'] = x2
        return redirect(dashboard)




    return render_template('calc.html', title='Logowanie', login=login)

@app.route('/logOut')
def logOut():
    session.pop('userLogin')
    return redirect('logIn')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html', title='Dashboard', userLogin=session.get('userLogin'))

# uruchomienie aplikacji
if __name__ == '__main__':
    app.run(debug=True)

