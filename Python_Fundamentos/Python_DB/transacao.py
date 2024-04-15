import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

conexao = sqlite3.connect(f"{ROOT_PATH}/meu_banco.db") # Cria o banco de dados
cursor = conexao.cursor() # Cursor para executar comandos SQL
cursor.row_factory = sqlite3.Row

try:
    cursor.execute('INSERT INTO clientes (nome, email) VALUES (?,?);', ('Teste 3', 'teste3@gmail.com'))
    cursor.execute('INSERT INTO clientes (nome, email) VALUES (?,?);', (2, 'Teste 1', 'teste@gmail.com'))
    conexao.commit()
except Exception as exc:
    print(f"Ops! um erro ocorreu! {exc}")
    conexao.rollback()
