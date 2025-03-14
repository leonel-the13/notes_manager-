from datetime import datetime

class Nota:
    def __init__(self, titulo, texto):
        self.titulo = titulo
        self.texto = texto
        self.data_de_criacao = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def __str__(self):
        print(f'\033[1;37mTítulo: {self.titulo} \033[0m(Cirado em: \033[33m{self.data_de_criacao}\033[0m)\nConteúdo: {self.texto}\n')