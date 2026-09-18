from conexao import conectar

def cadastrar_produto(nome, descricao, preco, estoque):
    conexao = conectar()
    if not conexao:
        return
    
    try:
        cursor = conexao.cursor()
        sql = "INSERT INTO produtos (nome, descricao, preco, estoque) VALUES (%s, %s, %s, %s)"
        valores = (nome, descricao, preco, estoque)
        cursor.execute(sql, valores)
        conexao.commit()
        print(f"\nProduto \x27{nome}\x27 cadastrado com sucesso!")
    except Exception as e:
        print(f"\nErro ao cadastrar produto: {e}")
    finally:
        cursor.close()
        conexao.close()

def listar_produtos():
    conexao = conectar()
    if not conexao:
        return

    try:
        cursor = conexao.cursor()
        cursor.execute("SELECT id, nome, descricao, preco, estoque, criado_em FROM produtos")
        resultados = cursor.fetchall()
        
        print("\n--- LISTA DE PRODUTOS CADASTRADOS ---")
        if not resultados:
            print("Nenhum produto cadastrado ainda.")
        for (id, nome, descricao, preco, estoque, criado_em) in resultados:
            print(f"ID: {id} | Nome: {nome} | Desc: {descricao} | Preço: R$ {preco:.2f} | Estoque: {estoque}")
        print("-" * 50)
    except Exception as e:
        print(f"\nErro ao listar produtos: {e}")
    finally:
        cursor.close()
        conexao.close()

def atualizar_produto(produto_id, novo_nome, nova_desc, novo_preco, novo_estoque):
    conexao = conectar()
    if not conexao:
        return

    try:
        cursor = conexao.cursor()
        sql = "UPDATE produtos SET nome = %s, descricao = %s, preco = %s, estoque = %s WHERE id = %s"
        valores = (novo_nome, nova_desc, novo_preco, novo_estoque, produto_id)
        cursor.execute(sql, valores)
        conexao.commit()
        
        if cursor.rowcount > 0:
            print(f"\nProduto ID {produto_id} atualizado com sucesso!")
        else:
            print(f"\nNenhum produto encontrado com o ID {produto_id}.")
    except Exception as e:
        print(f"\nErro ao atualizar produto: {e}")
    finally:
        cursor.close()
        conexao.close()

def deletar_produto(produto_id):
    conexao = conectar()
    if not conexao:
        return

    try:
        cursor = conexao.cursor()
        sql = "DELETE FROM produtos WHERE id = %s"
        cursor.execute(sql, (produto_id,))
        conexao.commit()
        
        if cursor.rowcount > 0:
            print(f"\nProduto ID {produto_id} removido com sucesso!")
        else:
            print(f"\nNenhum produto encontrado com o ID {produto_id}.")
    except Exception as e:
        print(f"\nErro ao deletar produto: {e}")
    finally:
        cursor.close()
        conexao.close()
