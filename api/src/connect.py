import mysql.connector
from api.src.model import Pessoa
from flask import jsonify

conexao = mysql.connector.connect(
    host = 'monorail.proxy.rlwy.net',
    user =  'root',
    password = 'dh3g6-Fh1e46CddaeA66aBbBD33a3H6d',
    database = 'railway',
    port = 34731
)
cursor = conexao.cursor()

def inserir(model:Pessoa):
    comando = "CREATE TABLE IF NOT EXISTS cadastros (nome varchar(40),dia date,hora time) "
    cursor.execute(comando)
    conexao.commit()
    cursor.execute(f'INSERT INTO cadastros (nome,dia,hora) VALUES ("%s",%s,%s)',(model.nome,model.dia,model.hora))
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