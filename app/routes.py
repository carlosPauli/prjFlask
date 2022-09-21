from operator import index
from app import app;
from flask import render_template;


@app.route("/")
@app.route("/index")
def hello():
    usuario = {'nome': 'Carlos'}
    disciplinas = [
        {'nome': 'Logica'},
        {'nome': 'BDA'},
        {'nome': 'Flask'},
        {'nome': 'Python'},
    ]
    return render_template('index.html', titulo ='Aula 01 - WebDev with a flask', usuario=usuario, disciplinas=disciplinas)