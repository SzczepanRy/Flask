from flask import Flask, render_template, request
from flask_assets import Environment, Bundle


import time

import RPi.GPIO as GPIO
# import RPi.GPIO as GPIO

# channel =21
# GPIO.setmode(GPIO.HIGH)
# GPIO.setup(channel,GPIO.HIGH)





app=Flask(__name__)

assets = Environment(app)
assets.url = app.static_url_path

scss = Bundle(
    "assets/scss/login.scss",
    "assets/scss/index.scss",
    "assets/scss/bomb.scss",
    filters="pyscss",
    output="all.css",
)
assets.register("style", scss)

bombs = ["bomb 1 (shool)" , "bomb 2 (jabobs house)", " bomb 3 (math class)"]
user = {"login":"a","password":"a"}


def bomb():
    relay_ch = 18
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)

    GPIO.setup(relay_ch, GPIO.OUT)
    GPIO.output(relay_ch, GPIO.LOW)
    time.sleep(1)
    GPIO.output(relay_ch, GPIO.HIGH)
    GPIO.cleanup()



@app.route("/", methods=["GET"])
def login():
    return render_template("login.html")

@app.route("/login",methods=["POST"])
def home():
    login = request.form["login"]
    password = request.form["password"]
    if(login == user["login"] and password == user["password"]):
        return render_template("index.html" , bombs=bombs)
    else:
        return render_template("login.html")


@app.route("/detonate", methods=["POST"])
def detonate():
    bombL = request.form["location"]
    print(bombL)
    if bombL:
        #detonate bomb 
        bomb()
             

        return render_template("bomb.html",bomb=bombL)
        
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=2137)