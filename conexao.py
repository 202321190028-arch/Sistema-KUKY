import mysql.connector
from mysql.connector import Error

try:
    conexao = mysql.connector.connect(
        host='localhost',
        database='db_kuky',
        user='root',
        password='123456'
    )

    if conexao.is_connected():
        db_info = conexao.server_info
        print(f"Conectado com sucesso ao servidor MySQL Versão: {db_info}")
        cursor = conexao.cursor()
        cursor.execute("SELECT DATABASE();")
        linha = cursor.fetchone()
        print(f"Conectado ao banco de dados: {linha[0]}")

except Error as e:
    print(f"Erro ao conectar ao MySQL: {e}")

finally:
    if 'conexao' in locals() and conexao.is_connected():
        cursor.close()
        conexao.close()
        print("Conexão MySQL encerrada.")
