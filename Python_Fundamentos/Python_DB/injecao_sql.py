import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

conexao = sqlite3.connect(f"{ROOT_PATH}/meu_banco.db") # Cria o banco de dados
cursor = conexao.cursor() # Cursor para executar comandos SQL
cursor.row_factory = sqlite3.Row

id_cliente = input('Informe o ID do cliente: ')
cliente = cursor.execute(f'SELECT * FROM clientes WHERE id = {id_cliente}')
cliente = cursor.fetchone()
print(dict(cliente))