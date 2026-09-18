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
        print(f"\nCliente \x27{nome}\x27 cadastrado com sucesso!")
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

def atualizar_cliente(cliente_id, novo_nome, novo_doc, novo_tel, novo_email):
    conexao = conectar()
    if not conexao:
        return

    try:
        cursor = conexao.cursor()
        sql = "UPDATE clientes SET nome = %s, documento = %s, telefone = %s, email = %s WHERE id = %s"
        valores = (novo_nome, novo_doc, novo_tel, novo_email, cliente_id)
        cursor.execute(sql, valores)
        conexao.commit()
        
        if cursor.rowcount > 0:
            print(f"\nCliente ID {cliente_id} atualizado com sucesso!")
        else:
            print(f"\nNenhum cliente encontrado com o ID {cliente_id}.")
    except Exception as e:
        print(f"\nErro ao atualizar cliente: {e}")
    finally:
        cursor.close()
        conexao.close()

def deletar_cliente(cliente_id):
    conexao = conectar()
    if not conexao:
        return

    try:
        cursor = conexao.cursor()
        sql = "DELETE FROM clientes WHERE id = %s"
        cursor.execute(sql, (cliente_id,))
        conexao.commit()
        
        if cursor.rowcount > 0:
            print(f"\nCliente ID {cliente_id} removido com sucesso!")
        else:
            print(f"\nNenhum cliente encontrado com o ID {cliente_id}.")
    except Exception as e:
        print(f"\nErro ao deletar cliente: {e}")
    finally:
        cursor.close()
        conexao.close()
