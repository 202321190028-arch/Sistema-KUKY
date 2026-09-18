from crud import cadastrar_usuario, listar_usuarios, atualizar_usuario, deletar_usuario
from crud_clientes import cadastrar_cliente, listar_clientes, atualizar_cliente, deletar_cliente
from crud_produtos import cadastrar_produto, listar_produtos, atualizar_produto, deletar_produto
from crud_pedidos import criar_pedido, listar_pedidos

def exibir_menu_principal():
    print("\n" + "="*40)
    print("       SISTEMA-KUKY - MENU PRINCIPAL")
    print("="*40)
    print("1. Gerenciar Usuários")
    print("2. Gerenciar Clientes")
    print("3. Gerenciar Produtos")
    print("4. Gerenciar Pedidos")
    print("0. Sair")
    print("="*40)

def menu_usuarios():
    while True:
        print("\n--- GERENCIAR USUÁRIOS ---")
        print("1. Cadastrar novo usuário")
        print("2. Listar usuários")
        print("3. Atualizar usuário")
        print("4. Deletar usuário")
        print("0. Voltar ao menu principal")
        
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == "1":
            nome = input("Digite o nome: ")
            email = input("Digite o e-mail: ")
            cadastrar_usuario(nome, email)
        elif opcao == "2":
            listar_usuarios()
        elif opcao == "3":
            listar_usuarios()
            user_id = input("Digite o ID do usuário que deseja atualizar: ")
            novo_nome = input("Digite o novo nome: ")
            novo_email = input("Digite o novo e-mail: ")
            atualizar_usuario(user_id, novo_nome, novo_email)
        elif opcao == "4":
            listar_usuarios()
            user_id = input("Digite o ID do usuário que deseja remover: ")
            confirmacao = input(f"Tem certeza que deseja apagar o usuário ID {user_id}? (s/n): ").lower()
            if confirmacao == "s":
                deletar_usuario(user_id)
            else:
                print("Operação cancelada.")
        elif opcao == "0":
            break
        else:
            print("Opção inválida!")

def menu_clientes():
    while True:
        print("\n--- GERENCIAR CLIENTES ---")
        print("1. Cadastrar novo cliente")
        print("2. Listar clientes")
        print("3. Atualizar cliente")
        print("4. Deletar cliente")
        print("0. Voltar ao menu principal")
        
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == "1":
            nome = input("Digite o nome do cliente: ")
            documento = input("Digite o CPF ou CNPJ: ")
            telefone = input("Digite o telefone: ")
            email = input("Digite o e-mail: ")
            cadastrar_cliente(nome, documento, telefone, email)
        elif opcao == "2":
            listar_clientes()
        elif opcao == "3":
            listar_clientes()
            cliente_id = input("Digite o ID do cliente que deseja atualizar: ")
            novo_nome = input("Digite o novo nome: ")
            novo_doc = input("Digite o novo documento: ")
            novo_tel = input("Digite o novo telefone: ")
            novo_email = input("Digite o novo e-mail: ")
            atualizar_cliente(cliente_id, novo_nome, novo_doc, novo_tel, novo_email)
        elif opcao == "4":
            listar_clientes()
            cliente_id = input("Digite o ID do cliente que deseja remover: ")
            confirmacao = input(f"Tem certeza que deseja apagar o cliente ID {cliente_id}? (s/n): ").lower()
            if confirmacao == "s":
                deletar_cliente(cliente_id)
            else:
                print("Operação cancelada.")
        elif opcao == "0":
            break
        else:
            print("Opção inválida!")

def menu_produtos():
    while True:
        print("\n--- GERENCIAR PRODUTOS ---")
        print("1. Cadastrar novo produto")
        print("2. Listar produtos")
        print("3. Atualizar produto")
        print("4. Deletar produto")
        print("0. Voltar ao menu principal")
        
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == "1":
            nome = input("Digite o nome do produto: ")
            descricao = input("Digite a descrição: ")
            preco = float(input("Digite o preço (ex: 49.90): "))
            estoque = int(input("Digite a quantidade em estoque: "))
            cadastrar_produto(nome, descricao, preco, estoque)
        elif opcao == "2":
            listar_produtos()
        elif opcao == "3":
            listar_produtos()
            prod_id = input("Digite o ID do produto que deseja atualizar: ")
            novo_nome = input("Digite o novo nome: ")
            nova_desc = input("Digite a nova descrição: ")
            novo_preco = float(input("Digite o novo preço: "))
            novo_estoque = int(input("Digite o novo estoque: "))
            atualizar_produto(prod_id, novo_nome, nova_desc, novo_preco, novo_estoque)
        elif opcao == "4":
            listar_produtos()
            prod_id = input("Digite o ID do produto que deseja remover: ")
            confirmacao = input(f"Tem certeza que deseja apagar o produto ID {prod_id}? (s/n): ").lower()
            if confirmacao == "s":
                deletar_produto(prod_id)
            else:
                print("Operação cancelada.")
        elif opcao == "0":
            break
        else:
            print("Opção inválida!")

def menu_pedidos():
    while True:
        print("\n--- GERENCIAR PEDIDOS ---")
        print("1. Criar novo pedido")
        print("2. Listar pedidos e detalhes")
        print("0. Voltar ao menu principal")
        
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == "1":
            listar_clientes()
            cliente_id = input("Digite o ID do cliente que está comprando: ")
            
            itens = []
            while True:
                listar_produtos()
                prod_id = input("Digite o ID do produto (ou \x270\x27 para finalizar os itens): ").strip()
                if prod_id == "0":
                    break
                qtd = int(input("Digite a quantidade desejada: "))
                itens.append((prod_id, qtd))
                
                continuar = input("Adicionar outro produto ao pedido? (s/n): ").lower()
                if continuar != "s":
                    break
            
            if itens:
                criar_pedido(cliente_id, itens)
            else:
                print("Nenhum item adicionado. Pedido cancelado.")
                
        elif opcao == "2":
            listar_pedidos()
        elif opcao == "0":
            break
        else:
            print("Opção inválida!")

def main():
    while True:
        exibir_menu_principal()
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == "1":
            menu_usuarios()
        elif opcao == "2":
            menu_clientes()
        elif opcao == "3":
            menu_produtos()
        elif opcao == "4":
            menu_pedidos()
        elif opcao == "0":
            print("\nSaindo do Sistema-KUKY. Até mais!")
            break
        else:
            print("\nOpção inválida! Escolha entre 0 e 4.")

if __name__ == "__main__":
    main()
