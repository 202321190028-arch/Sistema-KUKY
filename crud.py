from conexao import conectar

def cadastrar_usuario(nome, email):
    conexao = conectar()
    if not conexao:
        return
    
    try:
        cursor = conexao.cursor()
        sql = "INSERT INTO usuarios (nome, email) VALUES (%s, %s)"
        valores = (nome, email)
        cursor.execute(sql, valores)
        conexao.commit()
        print(f"\nUsuário '{nome}' cadastrado com sucesso!")
    except Exception as e:
        print(f"\nErro ao cadastrar usuário: {e}")
    finally:
        cursor.close()
        conexao.close()

def listar_usuarios():
    conexao = conectar()
    if not conexao:
        return

    try:
        cursor = conexao.cursor()
        cursor.execute("SELECT id, nome, email, criado_em FROM usuarios")
        resultados = cursor.fetchall()
        
        print("\n--- LISTA DE USUÁRIOS CADASTRADOS ---")
        if not resultados:
            print("Nenhum usuário cadastrado ainda.")
        for (id, nome, email, criado_em) in resultados:
            print(f"ID: {id} | Nome: {nome} | E-mail: {email} | Criado em: {criado_em}")
        print("-" * 40)
    except Exception as e:
        print(f"\nErro ao listar usuários: {e}")
    finally:
        cursor.close()
        conexao.close()

def atualizar_usuario(user_id, novo_nome, novo_email):
    conexao = conectar()
    if not conexao:
        return

    try:
        cursor = conexao.cursor()
        sql = "UPDATE usuarios SET nome = %s, email = %s WHERE id = %s"
        valores = (novo_nome, novo_email, user_id)
        cursor.execute(sql, valores)
        conexao.commit()
        
        if cursor.rowcount > 0:
            print(f"\nUsuário ID {user_id} atualizado com sucesso!")
        else:
            print(f"\nNenhum usuário encontrado com o ID {user_id}.")
    except Exception as e:
        print(f"\nErro ao atualizar usuário: {e}")
    finally:
        cursor.close()
        conexao.close()

def deletar_usuario(user_id):
    conexao = conectar()
    if not conexao:
        return

    try:
        cursor = conexao.cursor()
        sql = "DELETE FROM usuarios WHERE id = %s"
        cursor.execute(sql, (user_id,))
        conexao.commit()
        
        if cursor.rowcount > 0:
            print(f"\nUsuário ID {user_id} removido com sucesso!")
        else:
            print(f"\nNenhum usuário encontrado com o ID {user_id}.")
    except Exception as e:
        print(f"\nErro ao deletar usuário: {e}")
    finally:
        cursor.close()
        conexao.close()

if __name__ == "__main__":
    print("Testando o CRUD completo do Sistema-KUKY:")
    listar_usuarios()
