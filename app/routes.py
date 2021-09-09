from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():

    projeto = {"nome": "Nutrif"}

    return render_template('index.html', projeto = projeto, titulo = 'Página inicial')

@app.route('/contato')
def contato():
    return render_template('contato.html', titulo='Microblog - contato')

@app.route('/sobre')
def sobre():
    return render_template('sobre.html', titulo='Microblog - sobre')