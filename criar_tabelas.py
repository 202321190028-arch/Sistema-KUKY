from conexao import conectar

def criar_tabelas_extras():
    conexao = conectar()
    if conexao and conexao.is_connected():
        cursor = conexao.cursor()
        
        # Tabela de Clientes
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS clientes (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nome VARCHAR(100) NOT NULL,
                email VARCHAR(100),
                telefone VARCHAR(20)
            )
        """)
        
        # Tabela de Pedidos
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS pedidos (
                id INT AUTO_INCREMENT PRIMARY KEY,
                cliente_id INT,
                produto_id INT,
                quantidade INT NOT NULL,
                data_pedido TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (cliente_id) REFERENCES clientes(id),
                FOREIGN KEY (produto_id) REFERENCES produtos(id)
            )
        """)
        
        conexao.commit()
        cursor.close()
        conexao.close()
        print("Sucesso! Tabelas 'clientes' e 'pedidos' criadas (ou já existentes) no MySQL.")
    else:
        print("Erro: Não foi possível conectar ao banco de dados.")

if __name__ == "__main__":
    criar_tabelas_extras()
