from app import app
from flask import render_template

@app.route("/")

def index():
    nome = "Everton da Silva"
    dados = {"profissao": "Programador", "formacao": "Análise e Desenvolvimento de Sistemas"}
    return render_template("index.html", nome = nome, dados = dados)

@app.route('/contato')
def contato():
    return render_template("contato.html")