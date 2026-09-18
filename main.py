from crud import cadastrar_usuario, listar_usuarios, atualizar_usuario, deletar_usuario
from crud_clientes import cadastrar_cliente, listar_clientes, atualizar_cliente, deletar_cliente

def exibir_menu_principal():
    print("\n" + "="*40)
    print("       SISTEMA-KUKY - MENU PRINCIPAL")
    print("="*40)
    print("1. Gerenciar Usuários")
    print("2. Gerenciar Clientes")
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
        
        if opcao == '1':
            nome = input("Digite o nome: ")
            email = input("Digite o e-mail: ")
            cadastrar_usuario(nome, email)
        elif opcao == '2':
            listar_usuarios()
        elif opcao == '3':
            listar_usuarios()
            user_id = input("Digite o ID do usuário que deseja atualizar: ")
            novo_nome = input("Digite o novo nome: ")
            novo_email = input("Digite o novo e-mail: ")
            atualizar_usuario(user_id, novo_nome, novo_email)
        elif opcao == '4':
            listar_usuarios()
            user_id = input("Digite o ID do usuário que deseja remover: ")
            confirmacao = input(f"Tem certeza que deseja apagar o usuário ID {user_id}? (s/n): ").lower()
            if confirmacao == 's':
                deletar_usuario(user_id)
            else:
                print("Operação cancelada.")
        elif opcao == '0':
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
        
        if opcao == '1':
            nome = input("Digite o nome do cliente: ")
            documento = input("Digite o CPF ou CNPJ: ")
            telefone = input("Digite o telefone: ")
            email = input("Digite o e-mail: ")
            cadastrar_cliente(nome, documento, telefone, email)
        elif opcao == '2':
            listar_clientes()
        elif opcao == '3':
            listar_clientes()
            cliente_id = input("Digite o ID do cliente que deseja atualizar: ")
            novo_nome = input("Digite o novo nome: ")
            novo_doc = input("Digite o novo documento: ")
            novo_tel = input("Digite o novo telefone: ")
            novo_email = input("Digite o novo e-mail: ")
            atualizar_cliente(cliente_id, novo_nome, novo_doc, novo_tel, novo_email)
        elif opcao == '4':
            listar_clientes()
            cliente_id = input("Digite o ID do cliente que deseja remover: ")
            confirmacao = input(f"Tem certeza que deseja apagar o cliente ID {cliente_id}? (s/n): ").lower()
            if confirmacao == 's':
                deletar_cliente(cliente_id)
            else:
                print("Operação cancelada.")
        elif opcao == '0':
            break
        else:
            print("Opção inválida!")

def main():
    while True:
        exibir_menu_principal()
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == '1':
            menu_usuarios()
        elif opcao == '2':
            menu_clientes()
        elif opcao == '0':
            print("\nSaindo do Sistema-KUKY. Até mais!")
            break
        else:
            print("\nOpção inválida! Escolha entre 0 e 2.")

if __name__ == "__main__":
    main()from crud import cadastrar_usuario, listar_usuarios, atualizar_usuario, deletar_usuario

def exibir_menu():
    print("\n" + "="*40)
    print("       SISTEMA-KUKY - MENU PRINCIPAL")
    print("="*40)
    print("1. Cadastrar novo usuário")
    print("2. Listar usuários cadastrados")
    print("3. Atualizar usuário")
    print("4. Deletar usuário")
    print("0. Sair")
    print("="*40)

def main():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == '1':
            print("\n--- CADASTRO DE NOVO USUÁRIO ---")
            nome = input("Digite o nome: ")
            email = input("Digite o e-mail: ")
            cadastrar_usuario(nome, email)
            
        elif opcao == '2':
            listar_usuarios()
            
        elif opcao == '3':
            print("\n--- ATUALIZAR USUÁRIO ---")
            listar_usuarios()
            user_id = input("Digite o ID do usuário que deseja atualizar: ")
            novo_nome = input("Digite o novo nome: ")
            novo_email = input("Digite o novo e-mail: ")
            atualizar_usuario(user_id, novo_nome, novo_email)
            
        elif opcao == '4':
            print("\n--- DELETAR USUÁRIO ---")
            listar_usuarios()
            user_id = input("Digite o ID do usuário que deseja remover: ")
            confirmacao = input(f"Tem certeza que deseja apagar o usuário ID {user_id}? (s/n): ").lower()
            if confirmacao == 's':
                deletar_usuario(user_id)
            else:
                print("Operação cancelada.")
                
        elif opcao == '0':
            print("\nSaindo do Sistema-KUKY. Até mais!")
            break
        else:
            print("\nOpção inválida! Escolha um número entre 0 e 4.")

if __name__ == "__main__":
    main()
from crud import cadastrar_usuario, listar_usuarios, atualizar_usuario, deletar_usuario

def exibir_menu():
    print("\n" + "="*40)
    print("       SISTEMA-KUKY - MENU PRINCIPAL")
    print("="*40)
    print("1. Cadastrar novo usuário")
    print("2. Listar usuários cadastrados")
    print("3. Atualizar usuário")
    print("4. Deletar usuário")
    print("0. Sair")
    print("="*40)

def main():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == '1':
            print("\n--- CADASTRO DE NOVO USUÁRIO ---")
            nome = input("Digite o nome: ")
            email = input("Digite o e-mail: ")
            cadastrar_usuario(nome, email)
            
        elif opcao == '2':
            listar_usuarios()
            
        elif opcao == '3':
            print("\n--- ATUALIZAR USUÁRIO ---")
            listar_usuarios()
            user_id = input("Digite o ID do usuário que deseja atualizar: ")
            novo_nome = input("Digite o novo nome: ")
            novo_email = input("Digite o novo e-mail: ")
            atualizar_usuario(user_id, novo_nome, novo_email)
            
        elif opcao == '4':
            print("\n--- DELETAR USUÁRIO ---")
            listar_usuarios()
            user_id = input("Digite o ID do usuário que deseja remover: ")
            confirmacao = input(f"Tem certeza que deseja apagar o usuário ID {user_id}? (s/n): ").lower()
            if confirmacao == 's':
                deletar_usuario(user_id)
            else:
                print("Operação cancelada.")
                
        elif opcao == '0':
            print("\nSaindo do Sistema-KUKY. Até mais!")
            break
        else:
            print("\nOpção inválida! Escolha um número entre 0 e 4.")

if __name__ == "__main__":
    main()
