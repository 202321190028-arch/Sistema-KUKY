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
