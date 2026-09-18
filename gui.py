import customtkinter as ctk
from tkinter import messagebox
from conexao import conectar

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

class AppKuky(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Sistema-KUKY - Painel Completo")
        self.geometry("900x650")

        # Sistema de Abas Expandido
        self.tabview = ctk.CTkTabview(self, width=850, height=600)
        self.tabview.pack(padx=20, pady=20)

        self.tab_produtos = self.tabview.add("Produtos")
        self.tab_clientes = self.tabview.add("Clientes")
        self.tab_pedidos = self.tabview.add("Pedidos")

        # Configura cada aba
        self.setup_aba_produtos()
        self.setup_aba_clientes()
        self.setup_aba_pedidos()

        # Carrega dados iniciais
        self.carregar_produtos()
        self.carregar_clientes()
        self.carregar_pedidos()

    # ==========================================
    # ABA 1: PRODUTOS (Cadastro, Listagem, Editar, Excluir)
    # ==========================================
    def setup_aba_produtos(self):
        self.frame_form = ctk.CTkFrame(self.tab_produtos)
        self.frame_form.pack(side="left", padx=10, pady=10, fill="y")

        ctk.CTkLabel(self.frame_form, text="Gerenciar Produtos", font=ctk.CTkFont(size=16, weight="bold")).pack(pady=10)
        
        self.prod_id_edit = ctk.CTkEntry(self.frame_form, placeholder_text="ID (Apenas para Edição)", width=220)
        self.prod_id_edit.pack(pady=5)

        self.prod_nome = ctk.CTkEntry(self.frame_form, placeholder_text="Nome", width=220)
        self.prod_nome.pack(pady=5)

        self.prod_desc = ctk.CTkEntry(self.frame_form, placeholder_text="Descrição", width=220)
        self.prod_desc.pack(pady=5)

        self.prod_preco = ctk.CTkEntry(self.frame_form, placeholder_text="Preço", width=220)
        self.prod_preco.pack(pady=5)

        self.prod_estoque = ctk.CTkEntry(self.frame_form, placeholder_text="Estoque", width=220)
        self.prod_estoque.pack(pady=5)

        ctk.CTkButton(self.frame_form, text="Salvar Novo", fg_color="green", command=self.salvar_produto).pack(pady=5)
        ctk.CTkButton(self.frame_form, text="Atualizar/Editar", fg_color="orange", text_color="black", command=self.editar_produto).pack(pady=5)
        ctk.CTkButton(self.frame_form, text="Excluir por ID", fg_color="red", command=self.excluir_produto).pack(pady=5)
        ctk.CTkButton(self.frame_form, text="Limpar Campos", fg_color="gray", command=self.limpar_campos_produto).pack(pady=5)

        self.frame_lista = ctk.CTkFrame(self.tab_produtos)
        self.frame_lista.pack(side="right", padx=10, pady=10, fill="both", expand=True)

        self.texto_produtos = ctk.CTkTextbox(self.frame_lista, width=500, height=480)
        self.texto_produtos.pack(pady=5)
        ctk.CTkButton(self.frame_lista, text="Recarregar Lista", command=self.carregar_produtos).pack(pady=5)

    def limpar_campos_produto(self):
        self.prod_id_edit.delete(0, 'end')
        self.prod_nome.delete(0, 'end')
        self.prod_desc.delete(0, 'end')
        self.prod_preco.delete(0, 'end')
        self.prod_estoque.delete(0, 'end')

    def salvar_produto(self):
        nome, desc, preco, est = self.prod_nome.get(), self.prod_desc.get(), self.prod_preco.get(), self.prod_estoque.get()
        if not nome or not preco or not est:
            messagebox.showerror("Erro", "Preencha Nome, Preço e Estoque!")
            return
        try:
            conexao = conectar()
            cursor = conexao.cursor()
            cursor.execute("INSERT INTO produtos (nome, descricao, preco, estoque) VALUES (%s, %s, %s, %s)", 
                           (nome, desc, float(preco.replace(',','.')), int(est)))
            conexao.commit()
            cursor.close()
            conexao.close()
            messagebox.showinfo("Sucesso", "Produto cadastrado!")
            self.limpar_campos_produto()
            self.carregar_produtos()
        except Exception as e:
            messagebox.showerror("Erro", str(e))

    def editar_produto(self):
        pid = self.prod_id_edit.get()
        if not pid:
            messagebox.showerror("Erro", "Informe o ID do produto que deseja editar!")
            return
        try:
            conexao = conectar()
            cursor = conexao.cursor()
            sql = "UPDATE produtos SET nome=%s, descricao=%s, preco=%s, estoque=%s WHERE id=%s"
            cursor.execute(sql, (self.prod_nome.get(), self.prod_desc.get(), float(self.prod_preco.get().replace(',','.')), int(self.prod_estoque.get()), int(pid)))
            conexao.commit()
            cursor.close()
            conexao.close()
            messagebox.showinfo("Sucesso", "Produto atualizado com sucesso!")
            self.carregar_produtos()
        except Exception as e:
            messagebox.showerror("Erro", str(e))

    def excluir_produto(self):
        pid = self.prod_id_edit.get()
        if not pid:
            messagebox.showerror("Erro", "Informe o ID do produto para exclusão!")
            return
        if messagebox.askyesno("Confirmar", f"Deseja realmente excluir o produto ID {pid}?"):
            try:
                conexao = conectar()
                cursor = conexao.cursor()
                cursor.execute("DELETE FROM produtos WHERE id = %s", (int(pid),))
                conexao.commit()
                cursor.close()
                conexao.close()
                messagebox.showinfo("Sucesso", "Produto excluído!")
                self.limpar_campos_produto()
                self.carregar_produtos()
            except Exception as e:
                messagebox.showerror("Erro", str(e))

    def carregar_produtos(self):
        self.texto_produtos.delete("0.0", "end")
        conexao = conectar()
        if conexao:
            cursor = conexao.cursor(dictionary=True)
            cursor.execute("SELECT id, nome, preco, estoque FROM produtos")
            produtos = cursor.fetchall()
            cursor.close()
            conexao.close()
            self.texto_produtos.insert("end", f"{'ID':<4} | {'NOME':<20} | {'PREÇO':<10} | {'ESTOQUE'}\n")
            self.texto_produtos.insert("end", "-" * 50 + "\n")
            for p in produtos:
                self.texto_produtos.insert("end", f"{p['id']:<4} | {p['nome']:<20} | R${p['preco']:<8.2f} | {p['estoque']}\n")

    # ==========================================
    # ABA 2: CLIENTES
    # ==========================================
    def setup_aba_clientes(self):
        ctk.CTkLabel(self.tab_clientes, text="Módulo de Clientes", font=ctk.CTkFont(size=16, weight="bold")).pack(pady=10)
        self.texto_clientes = ctk.CTkTextbox(self.tab_clientes, width=750, height=420)
        self.texto_clientes.pack(pady=10)
        ctk.CTkButton(self.tab_clientes, text="Atualizar Clientes", command=self.carregar_clientes).pack(pady=5)

    def carregar_clientes(self):
        self.texto_clientes.delete("0.0", "end")
        try:
            conexao = conectar()
            if conexao:
                cursor = conexao.cursor(dictionary=True)
                cursor.execute("SELECT * FROM clientes")
                clientes = cursor.fetchall()
                cursor.close()
                conexao.close()
                if not clientes:
                    self.texto_clientes.insert("end", "Nenhum cliente cadastrado.\n")
                else:
                    for c in clientes:
                        self.texto_clientes.insert("end", f"{c}\n")
            else:
                self.texto_clientes.insert("end", "Erro de conexão com o banco.\n")
        except Exception:
            self.texto_clientes.insert("end", "Tabela 'clientes' ainda não criada no banco MySQL.\n")

    # ==========================================
    # ABA 3: PEDIDOS
    # ==========================================
    def setup_aba_pedidos(self):
        ctk.CTkLabel(self.tab_pedidos, text="Módulo de Pedidos", font=ctk.CTkFont(size=16, weight="bold")).pack(pady=10)
        self.texto_pedidos = ctk.CTkTextbox(self.tab_pedidos, width=750, height=420)
        self.texto_pedidos.pack(pady=10)
        ctk.CTkButton(self.tab_pedidos, text="Atualizar Pedidos", command=self.carregar_pedidos).pack(pady=5)

    def carregar_pedidos(self):
        self.texto_pedidos.delete("0.0", "end")
        try:
            conexao = conectar()
            if conexao:
                cursor = conexao.cursor(dictionary=True)
                cursor.execute("SELECT * FROM pedidos")
                pedidos = cursor.fetchall()
                cursor.close()
                conexao.close()
                if not pedidos:
                    self.texto_pedidos.insert("end", "Nenhum pedido registrado.\n")
                else:
                    for p in pedidos:
                        self.texto_pedidos.insert("end", f"{p}\n")
            else:
                self.texto_pedidos.insert("end", "Erro de conexão com o banco.\n")
        except Exception:
            self.texto_pedidos.insert("end", "Tabela 'pedidos' ainda não criada no banco MySQL.\n")

if __name__ == "__main__":
    app = AppKuky()
    app.mainloop()
