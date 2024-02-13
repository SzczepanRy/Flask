from flask import Flask, render_template, request,Response
from flask_assets import Environment, Bundle
import os
import cv2
import subprocess
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

user = {"login":"a","password":"a"}
relay_ch = 18

def on():
 
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)

    GPIO.setup(relay_ch, GPIO.OUT)
    GPIO.output(relay_ch, GPIO.LOW)
    time.sleep(10*60*60*24)
    GPIO.cleanup()
def off():
    
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)

    GPIO.setup(relay_ch, GPIO.OUT)
    GPIO.output(relay_ch, GPIO.HIGH)
    time.sleep(10*60*60*24)
    GPIO.cleanup()
    



@app.route("/", methods=["GET"])
def login():
    return render_template("login.html")

@app.route("/login",methods=["POST"])
def home():
    login = request.form["login"]
    password = request.form["password"]
    if(login == user["login"] and password == user["password"]):
        return render_template("index.html")
    else:
        return render_template("login.html")
    
def gen():

    """Video streaming generator function."""
    
    vs = cv2.VideoCapture("tcp://192.168.8.104:8888")
    while True:
        try:
            ret,frame=vs.read()
            ret, jpeg = cv2.imencode('.jpg', frame)
            frame=jpeg.tobytes()
            yield (b'--frame\r\n'
            b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
        except Exception as err :
            subprocess.call(["libcamera-vid -t 0 --width 1920 --height 1080 --inline --listen -o tcp://192.168.8.104:8888"], shell=True)
            break
    vs.release()
    cv2.destroyAllWindows() 


@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(),mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route("/switch", methods=["POST"])
def switch():
    option = request.form["option"]
    if option == "on":
        on()
        #detonate bomb 
    if option == "off":
        off()             
    return render_template("bomb.html",option = option)
        
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=2137)