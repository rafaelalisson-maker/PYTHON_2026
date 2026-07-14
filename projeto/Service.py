from Cliente import Cliente
from Clientedao import Clientedao

class Service:
    __Clientedao = Clientedao()

    @staticmethod
    def cliente_inserir(nome, email, fone):
        cliente = Cliente(0, nome, email, fone)
        Service.__Clientedao.inserir(cliente)

    @staticmethod
    def cliente_listar():
        return Service.__Clientedao.listar()

    @staticmethod
    def cliente_listar_id(id):
        return Service.__Clientedao.listar_id(id)

    @staticmethod
    def cliente_listar_nome(iniciais):
        return Service.__Clientedao.listar_nome(iniciais)

    @staticmethod
    def cliente_atualizar(id, nome, email, fone):
        cliente = Cliente(id, nome, email, fone)
        Service.__Clientedao.atualizar(cliente)

    @staticmethod
    def cliente_excluir(id):
        Service.__Clientedao.excluir(id)