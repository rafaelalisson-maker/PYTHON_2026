import json
from Cliente import Cliente

class Clientedao:
    def __init__(self):
        self.__arquivo = "clientes.json"
        self.__objetos = []
        self.abrir()

    def inserir(self, cliente):
        if len(self.__objetos) == 0:
            cliente.set_id(1)
        else:
            maior = max(c.get_id() for c in self.__objetos)
            cliente.set_id(maior + 1)

        self.__objetos.append(cliente)
        self.salvar()

    def listar(self):
        return self.__objetos

    def listar_id(self, id):
        for c in self.__objetos:
            if c.get_id() == id:
                return c
        return None

    def listar_nome(self, iniciais):
        lista = []
        for c in self.__objetos:
            if c.get_nome().lower().startswith(iniciais.lower()):
                lista.append(c)
        return lista

    def atualizar(self, cliente):
        for i in range(len(self.__objetos)):
            if self.__objetos[i].get_id() == cliente.get_id():
                self.__objetos[i] = cliente
                self.salvar()
                return

    def excluir(self, id):
        cliente = self.listar_id(id)
        if cliente:
            self.__objetos.remove(cliente)
            self.salvar()

    def abrir(self):
        try:
            with open(self.__arquivo, "r") as f:
                dados = json.load(f)
                self.__objetos = [Cliente.from_json(c) for c in dados]
        except:
            self.__objetos = []

    def salvar(self):
        with open(self.__arquivo, "w") as f:
            json.dump([c.to_json() for c in self.__objetos], f, indent=4)