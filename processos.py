class Processos:
    def __init__(self):
        self.fila = []

    def adicionar_processo(self, id_processo, instrucoes):
        self.fila.append((id_processo, instrucoes))

    def get_fila_de_processos(self):
        return self.fila
