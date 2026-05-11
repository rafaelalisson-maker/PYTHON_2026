class time:
    def __init__(self, id, nome, estado):
        self.id = id
        self.nome = nome
        self.estado = estado
    
    def get_id(self):
        return self.id

    def set_nome(self, nome):
        self.nome = nome

    def set_estado(self, estado):
        self.estado = estado
    
    def __str__(self):
        return f"Time: {self.id} - {self.nome} ({self.estado})"

class jogador:
    def __int__(self, id, nome, camisa, id_time):
        self.id = id
        self.nome = nome
        self.camisa = camisa
        self.id_time = id_time
    
    def __str__(self):
        return f"Jogador: {self.id} - {self.nome} (Camisa: {self.camisa}, Time: {self.id_time})"

class UI:
    def __init__(self):
        self.times = []
        self.jogadores = []