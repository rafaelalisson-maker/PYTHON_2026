import json
class contato:
    def __init__(self, id, nome, email, fone, nascimento):
        self.id = id
        self.nome = nome
        self.email = email
        self.fone = fone
        self.nascimento = nascimento

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "email": self.email,
            "fone": self.fone,
            "nascimento": self.nascimento
        }
    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "email": self.email,
            "telefone": self.telefone,
            "nascimento": self.nascimento }
    
class ContatoUI:
    contatos = {}

    @staticmethod
    def inserir():
        id = int(input("ID: "))

        if id in ContatoUI.contatos:
            print("ID já cadastrado!")
            return

        nome = input("Nome: ")
        email = input("E-mail: ")
        telefone = input("Telefone: ")
        nascimento = input("Data de nascimento (dd/mm/aaaa): ")

        contatos = contatos (id, nome, email, telefone, nascimento)
        ContatoUI.contatos[id] = contato

        print("Contato cadastrado com sucesso!")

    @staticmethod
    def listar():
        if not ContatoUI.contatos:
            print("Nenhum contato cadastrado.")
            return

        for contato in ContatoUI.contatos.values():
            print(contato)