from conexao import conectar

def cadastrar_cliente(nome, documento, telefone, email):
    conexao = conectar()
    if not conexao:
        return
    
    try:
        cursor = conexao.cursor()
        sql = "INSERT INTO clientes (nome, documento, telefone, email) VALUES (%s, %s, %s, %s)"
        valores = (nome, documento, telefone, email)
        cursor.execute(sql, valores)
        conexao.commit()
        print(f"\nCliente '{nome}' cadastrado com sucesso!")
    except Exception as e:
        print(f"\nErro ao cadastrar cliente: {e}")
    finally:
        cursor.close()
        conexao.close()

def listar_clientes():
    conexao = conectar()
    if not conexao:
        return

    try:
        cursor = conexao.cursor()
        cursor.execute("SELECT id, nome, documento, telefone, email, criado_em FROM clientes")
        resultados = cursor.fetchall()
        
        print("\n--- LISTA DE CLIENTES CADASTRADOS ---")
        if not resultados:
            print("Nenhum cliente cadastrado ainda.")
        for (id, nome, documento, telefone, email, criado_em) in resultados:
            print(f"ID: {id} | Nome: {nome} | Doc: {documento} | Tel: {telefone} | E-mail: {email}")
        print("-" * 50)
    except Exception as e:
        print(f"\nErro ao listar clientes: {e}")
    finally:
        cursor.close()
        conexao.close()

if __name__ == "__main__":
    print("Testando o CRUD de Clientes:")
    cadastrar_cliente("Supermercado Exemplo", "12.345.678/0001-99", "(77) 99999-9999", "contato@exemplo.com")
    listar_clientes()
