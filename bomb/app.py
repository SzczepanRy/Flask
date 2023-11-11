from flask import Flask, render_template, request
import time
# import RPi.GPIO as GPIO

# channel =21
# GPIO.setmode(GPIO.HIGH)
# GPIO.setup(channel,GPIO.HIGH)



app=Flask(__name__)


bombs = ["bomb 1 (shool)" , "bomb 2 (jabobs house)", " bomb 3 (math class)"]
user = {"login":"a","password":"a"}


# def bomb():
#     time.sleep(1000)
#     GPIO.outupt(pin,GPIO.HIGH)
#     time.sleep(1000)
#     GPIO.outupt(pin,GPIO.LOW)



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
    if bombL:
        #detonate bomb 
        # bomb()
             

        return render_template("bomb.html",bomb=bombL)
        
if __name__ == '__main__':
    app.run(debug=True)