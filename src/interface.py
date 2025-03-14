import tkinter as tk
from tkinter import messagebox
from src.grencioador import GerenciadorNotas

class interfaceUsuario:
    def __init__(self, root):
        self.root = root
        self.root.title("Gerenciador de Notas")
        self.root.geometry("400x500")

        self.gerenciador = GerenciadorNotas()

        #titulo
        self.label_titulo = tk.Label(root, text="Título:")
        self.label_titulo.pack()
        self.entry_titulo = tk.Entry(root)
        self.entry_titulo.pack()

        #texto
        self.label_texto = tk.Label(root, text="Texto:")
        self.label_texto.pack()
        self.entry_texto = tk.Text(root, height=5, width=40)
        self.entry_texto.pack()

        #botao para adicionar nota
        self.btn_adicionar = tk.Button(root, text="Adicionar Nota", command=self.adicionar_nota)
        self.btn_adicionar.pack()

        #botao para exibir nota
        self.btn_visualizar = tk.Button(root, text="Visualizar Nota", command=self.visualizar_nota)
        self.btn_visualizar.pack(pady=5)

        #lista de notas
        self.labe_lista = tk.Label(root, text="Notas salvas:")
        self.labe_lista.pack()
        self.listbox_notas = tk.Listbox(root)
        self.listbox_notas.pack(fill=tk.BOTH, expand=True)

        #botao de excluir uma nota 
        self.btn_excluir = tk.Button(root, text="Exluir Nota", command=self.excluir_nota)
        self.btn_excluir.pack()

        #botao para listar as notas
        self.btn_listar = tk.Button(root, text="Listar Notas", command=self.listar_notas)
        self.btn_listar.pack()

        self.atualizar_lista()

    def adicionar_nota(self):
        titulo = self.entry_titulo.get()
        texto = self.entry_texto.get("1.0", tk.END)
        if titulo and texto:
            self.gerenciador.adicionar_notas(titulo, texto)
            messagebox.showinfo("Sucesso", "Nota adicionada com sucesso!")
            self.entry_titulo.delete(0, tk.END)
            self.entry_texto.delete("1.0", tk.END)
            self.atualizar_lista()
        else:
            messagebox.showerror("Erro", "Por favor, preencha todos os campos!")

    def visualizar_nota(self):
        selecionado = self.listbox_notas.curselection()
        if selecionado:
            index = selecionado[0]
            nota = self.gerenciador.notas[index]
            messagebox.showinfo(nota['titulo'], nota['texto'])
        else:
            messagebox.showerror("Erro", "Selecione uma nota para visualizar!")

    def listar_notas(self):
        #janela temporaria
        if hasattr(self, 'lista_tmp'):
            self.lista_tmp.destroy()
        self.lista_tmp = tk.Toplevel()
        self.lista_tmp.title("Lista de Notas")
        self.lista_tmp.geometry("300x300")
        self.label = tk.Label(self.lista_tmp, text="Lista de Notas:", font=("Arial", 14))
        self.label.pack()
        self.listbox = tk.Listbox(self.lista_tmp)
        self.listbox.pack(fill=tk.BOTH, expand=True)
        for nota in self.gerenciador.notas:
            self.listbox.insert(tk.END, nota['titulo'])

    def excluir_nota(self):
        selecionado = self.listbox_notas.curselection()
        if selecionado:
            index = selecionado[0]
            messagebox.showinfo("Excluir", "Nota excluída com sucesso!")
            self.gerenciador.exluir_nota(index)
            self.atualizar_lista()
        else:
            messagebox.showerror("Erro", "Selecione uma nota para excluir!")

    def atualizar_lista(self):
        self.listbox_notas.delete(0, tk.END)
        for nota in self.gerenciador.notas:
            self.listbox_notas.insert(tk.END, nota['titulo'])
        