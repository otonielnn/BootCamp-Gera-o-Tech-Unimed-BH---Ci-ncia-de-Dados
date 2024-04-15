import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

conexao = sqlite3.connect(f"{ROOT_PATH}/meu_banco.db") # Cria o banco de dados
cursor = conexao.cursor() # Cursor para executar comandos SQL
cursor.row_factory = sqlite3.Row

def criar_trabela(cursor):
    cursor.execute(
        'CREATE TABLE clientes(id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100), email VARCHAR(150));'
    ) # Criando tabela


def inserir_registro(conexao, cursor, nome, email):
    data = (nome, email)
    cursor.execute('INSERT INTO clientes(nome, email) values (?,?);', data)
    conexao.commit()

def atualizar_registro(conexao, cursor, nome, email, id):
    data = (nome, email, id)
    cursor.execute('UPDATE clientes SET nome = ?, email = ? WHERE id = ?;', data)
    conexao.commit()

def exlcuir_registro(conexao, cursor, id):
    data = (id,)
    cursor.execute('DELETE FROM clientes WHERE id = ?;', data)
    conexao.commit()

def inserir_muitos(conexao, cursor, dados):
    cursor.executemany('INSERT INTO clientes (nome, email) values (?,?);', dados)
    conexao.commit()

def recuperar_cliente(cursor, id):
    cursor.execute('SELECT * FROM clientes WHERE id = ?;', (id,))
    return cursor.fetchone()

def listar_clientes(cursor):
    return cursor.execute('SELECT * FROM clientes ORDER BY nome;')

cliente = recuperar_cliente(cursor, 1)
print(dict(cliente))

clientes = listar_clientes(cursor)
for cliente in clientes:
    print(dict(cliente))

# dados = [
#     ('Guilherme', 'guilherme@email.com'),
#     ('Jorge', 'Jorge@email.com'),
#     ('Isabela', 'isabela@email.com'),
#     ('Maria', 'maria@email.com')
# ]
# inserir_muitos(conexao, cursor, dados)