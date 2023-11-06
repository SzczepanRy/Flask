#import modulow i klas
from flask import Flask, render_template
from flask_bs4 import  Bootstrap


#konfig app
app = Flask(__name__)
bootstrap = Bootstrap(app)

#glowna czesc app

@app.route('/')
def index():
    return render_template('index.html', title='Home')

@app.errorhandler(404)
def pageNotFound(e):
    return render_template('404.html', title='nie ma takiej strony'), 404

@app.errorhandler(500)
def serverError(e):
    return render_template('500.html', title="wewnętrzny błąd serwera"), 500

#uruchamianie app
if __name__ == '__main__':
    app.run(debug=True, port=5001)
