import mysql.connector
from model import Pessoa
from flask import jsonify

conexao = mysql.connector.connect(
    host = 'localhost',
    user =  'root',
    password = 'minhasenha123',
    database = 'clientes',
    port = 3306
)
cursor = conexao.cursor()

def inserir(model:Pessoa):
    comando = "CREATE TABLE IF NOT EXISTS cadastros (nome varchar(40),dia INT,hora INT) "
    cursor.execute(comando)
    conexao.commit()
    cursor.execute(f'INSERT INTO cadastros VALUES ("{model.nome}",{model.dia},{model.hora})')
    conexao.commit()

def mostrardados():
    comando = "SELECT * FROM cadastros  "
    cursor.execute(comando)
    result = cursor.fetchall()
    dados = []
    for dado in result:
        dados.append(dado)

    return dados

'''def excluirdados(model:Pessoa):
    comando = f"DELETE FROM cadastros WHERE 'nome' = {model.nome} "
    cursor.execute(comando)
    print('sucesso')'''