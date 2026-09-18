import customtkinter as ctk
from tkinter import messagebox
from conexao import conectar

# Configuração inicial do tema do CustomTkinter
ctk.set_appearance_mode("System")  # Segue o tema do sistema (Dark/Light)
ctk.set_default_color_theme("blue")

class AppKuky(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Sistema-KUKY - Painel Visual")
        self.geometry("700x500")

        # Título da Tela
        self.label_titulo = ctk.CTkLabel(self, text="Gerenciamento - Sistema KUKY", font=ctk.CTkFont(size=20, weight="bold"))
        self.label_titulo.pack(pady=20)

        # Botão para testar a conexão com o Banco de Dados
        self.btn_conectar = ctk.CTkButton(self, text="Testar Conexão com o Banco", command=self.testar_conexao)
        self.btn_conectar.pack(pady=10)

        # Caixa de texto (Área de Log/Resultados)
        self.texto_saida = ctk.CTkTextbox(self, width=600, height=250)
        self.texto_saida.pack(pady=10)

    def testar_conexao(self):
        self.texto_saida.delete("0.0", "end") # Limpa a caixa
        conexao = conectar()
        if conexao and conexao.is_connected():
            self.texto_saida.insert("end", "Sucesso! Conectado ao banco de dados MySQL com sucesso.\n")
            
            # Exemplo de consulta rápida (como listar produtos)
            cursor = conexao.cursor()
            cursor.execute("SELECT COUNT(*) FROM produtos")
            qtd = cursor.fetchone()[0]
            self.texto_saida.insert("end", f"Total de produtos cadastrados no sistema: {qtd}\n")
            
            cursor.close()
            conexao.close()
        else:
            self.texto_saida.insert("end", "Erro: Não foi possível conectar ao banco de dados.\n")

if __name__ == "__main__":
    app = AppKuky()
    app.mainloop()
