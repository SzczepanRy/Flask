#import modulow i klas
from flask import Flask, render_template

#konfig app
app = Flask(__name__)

#glowna czesc app

@app.route('/')
def index():
    return '<h3>Hello FLask</h3>'

@app.route('/template')
def template():
    return render_template('template.html',title='Template')

@app.route('/user/<name>')
def user(name):
    return render_template('user.html',title='User', userName=name
    )

#uruchamianie app
if __name__ == '__main__':
    app.run(debug=True, port=5001)
