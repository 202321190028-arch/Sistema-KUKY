from conexao import conectar

def criar_pedido(cliente_id, itens):
    """
    itens deve ser uma lista de tuplas/dicionarios: [(produto_id, quantidade), ...]
    """
    conexao = conectar()
    if not conexao:
        return

    try:
        cursor = conexao.cursor()
        
        # Desativa o auto commit para controlar a transação manualmente
        conexao.start_transaction()

        # 1. Cria o pedido vinculado ao cliente
        sql_pedido = "INSERT INTO pedidos (cliente_id, status) VALUES (%s, \x27Concluído\x27)"
        cursor.execute(sql_pedido, (cliente_id,))
        pedido_id = cursor.lastrowid

        # 2. Processa cada item do pedido
        for produto_id, quantidade in itens:
            # Verifica o preço e o estoque atual do produto
            cursor.execute("SELECT preco, estoque FROM produtos WHERE id = %s", (produto_id,))
            produto = cursor.fetchone()
            
            if not produto:
                raise Exception(f"Produto ID {produto_id} não encontrado.")
            
            preco_unitario, estoque_atual = produto

            if estoque_atual < quantidade:
                raise Exception(f"Estoque insuficiente para o produto ID {produto_id}. Disponível: {estoque_atual}")

            # Insere o item na tabela relacional itens_pedido
            sql_item = "INSERT INTO itens_pedido (pedido_id, produto_id, quantidade, preco_unitario) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql_item, (pedido_id, produto_id, quantidade, preco_unitario))

            # Atualiza (baixa) o estoque do produto
            novo_estoque = estoque_atual - quantidade
            cursor.execute("UPDATE produtos SET estoque = %s WHERE id = %s", (novo_estoque, produto_id))

        # Confirma todas as operações da transação
        conexao.commit()
        print(f"\nPedido # {pedido_id} criado e estoque atualizado com sucesso!")

    except Exception as e:
        # Se houver qualquer erro, desfaz tudo para manter a consistência do banco
        conexao.rollback()
        print(f"\nErro ao criar pedido: {e}")
    finally:
        cursor.close()
        conexao.close()

def listar_pedidos():
    conexao = conectar()
    if not conexao:
        return

    try:
        cursor = conexao.cursor()
        sql = """
            SELECT p.id, c.nome, p.status, p.data_pedido 
            FROM pedidos p 
            JOIN clientes c ON p.cliente_id = c.id
        """
        cursor.execute(sql)
        pedidos = cursor.fetchall()
        
        print("\n--- LISTA DE PEDIDOS ---")
        if not pedidos:
            print("Nenhum pedido cadastrado ainda.")
        for (pedido_id, cliente_nome, status, data_pedido) in pedidos:
            print(f"Pedido ID: {pedido_id} | Cliente: {cliente_nome} | Status: {status} | Data: {data_pedido}")
            
            # Lista os itens do pedido
            cursor.execute("""
                SELECT pr.nome, ip.quantidade, ip.preco_unitario 
                FROM itens_pedido ip 
                JOIN produtos pr ON ip.produto_id = pr.id 
                WHERE ip.pedido_id = %s
            """, (pedido_id,))
            itens = cursor.fetchall()
            for (prod_nome, qtd, preco) in itens:
                print(f"   -> {prod_nome} | Qtd: {qtd} | Preço Unit.: R$ {preco:.2f}")
            print("-" * 40)
    except Exception as e:
        print(f"\nErro ao listar pedidos: {e}")
    finally:
        cursor.close()
        conexao.close()
