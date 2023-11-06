#import modulow i klas
from flask import Flask, render_template,session ,redirect
from flask_bs4 import  Bootstrap
from flask_wtf import  FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired
import math


#konfig app
app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config["SECRET_KEY"]="Hyogypsdafdohaidasuhisdaovhnjl";

class LoginForm(FlaskForm):

    A = StringField("A" , validators=[DataRequired()])
    B = StringField("B" , validators=[DataRequired()])
    C = StringField("C" , validators=[DataRequired()])
    submit = SubmitField("Policz miejsca zerowe")

#glowna czesc app
# users = {
#     "userLogin": "aslusarczyk",
#     "userPass": "Qwerty123!",
#     "firstName": "Adam",
#     "lastName": "Ślusarczyk"
# }






@app.route('/')
def index():
    return render_template('index.html', title='Home')


@app.route("/login",methods=["POST","GET"])
def logIn():
    login=LoginForm()
    if login.validate_on_submit():
        a = float(login.A.data)
        b = float(login.B.data)
        c = float(login.C.data)

        session["a"] = a
        session["b"] = b
        session["c"] = c


        if(a != 0):

            delta = (b ** 2) - (4 * a * c)
            session["delta"] = delta
            if delta > 0:
                x1 = (-b - math.sqrt(delta)) / (2 * a)
                x2 = (-b + math.sqrt(delta)) / (2 * a)
                session["x1"] = round(x1, 2)
                session["x2"] = round(x2, 2)
                print('x1 = '), x1, ("x2= "), x2
            elif delta == 0:
                x1 = -b / (2 * a)
                x2 = "brak miejsca zerowego"
                session["x1"] = round(x1, 2)
                session["x2"] = x2

            else:
                x1 = 'brak miejsca zerowego'
                x2 = "brak miejsca zerowego"
                session["x1"] = x1
                session["x2"] = x2
            return redirect("dashboard")
    return render_template('login.html', title='Logowanie',login=login)


@app.route("/logOut")
def logOut():
    session.pop('x1')
    session.pop('x2')
    session.pop('delta')
    return redirect("login")



@app.route("/dashboard")
def dashboard():
    # return  render_template("dashboard.html",title="dash",userLogin=session.get("userLogin"))

    return  render_template("dashboard.html",title="dash",x1=session.get("x1"),x2=session.get("x2"),delta=session.get("delta"))


#uruchamianie app
if __name__ == '__main__':
    app.run(debug=True, port=5002)
