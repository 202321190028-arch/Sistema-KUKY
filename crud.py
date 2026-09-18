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

if __name__ == "__main__":
    cadastrar_usuario("Lucas", "lucas@example.com")
    listar_usuarios()
