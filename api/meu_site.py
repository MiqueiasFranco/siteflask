from flask import Flask,render_template,request
from connect import inserir

from model import Pessoa

app = Flask(__name__)

# criar a pagina do site
@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/contatos")
def contatos():
    return render_template("contatos.html")

@app.route("/usuarios/<nome_usuario>")
def usuarios(nome_usuario):
    return render_template("usuarios.html",nome_usuario=nome_usuario)

@app.route("/")
def cadastrar():
    nome = request.form["nome"]
    dia = request.form["dia"]
    hora = request.form["hora"]
    pessoa = Pessoa(nome,dia,hora)
    inserir(pessoa)
    return render_template("homepage.html")


# coloca o site no ar 
if __name__=="__main__":
    app.run(debug=True)