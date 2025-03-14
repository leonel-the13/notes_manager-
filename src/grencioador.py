import json
import os
from src.notas import Nota

class GerenciadorNotas:
    def __init__(self, json_file="data/notas.json"):
        self.json_file = json_file
        self.notas = self.carregar_notas()

    def carregar_notas(self):
        if os.path.exists(self.json_file):
            with open(self.json_file, "r", encoding="utf-8") as file:
                return json.load(file)
        return []
    
    def salvar_notas(self):
        with open(self.json_file, "w", encoding="utf-8") as file:
            json.dump(self.notas, file, indent=4, ensure_ascii=False)

    def adicionar_notas(self, titulo, texto):
        nova_nota = Nota(titulo, texto).__dict__
        self.notas.append(nova_nota)
        self.salvar_notas()
        print("\033[1;32mNota adicionada com sucesso!\033[0m")

    def listar_notas(self):
        if not self.notas:
            print("Nenuma nota encontrada!")
            return 
        for idx, nota in enumerate(self.notas, start=1):
            print(f'\033[1;37m{idx}. {nota['titulo']} \033[0m(Criado em {nota['data_de_criacao']})')
    
    def editar_nota(self, index, novo_titulo, novo_text):
        if 0 <= index < len(self.notas):
            self.notas[index]['titulo'] = novo_titulo
            self.notas[index]['texto'] = novo_text
            self.salvar_notas()
            print("\033[1;32mAlteração realizada com sucesso!")
        else:
            print("\033[1;31mIdice inválido!")

    def buscar_nota(self, index):
        for nota in self.notas:
            if nota['titulo'] == index:
                return nota
            return None
        
    def exluir_nota(self, index):
        if 0 <= index < len(self.notas):
            del self.notas[index]
            self.salvar_notas()
            print("\033[1;32mNota eliminada com sucesso!")
        else:
            print("\033[1;31mIdice inválido!")