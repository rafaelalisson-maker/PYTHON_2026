from abc import ABC, abstractmethod


class DAO(ABC):
    def __init__(self):
        self._objetos = []
        self.abrir()

    @abstractmethod
    def abrir(self):
        raise NotImplementedError

    @abstractmethod
    def salvar(self):
        raise NotImplementedError

    def inserir(self, obj):
        maior_id = max(
            (item.get_id() for item in self._objetos),
            default=0
        )
        obj.set_id(maior_id + 1)
        self._objetos.append(obj)
        self.salvar()

    def listar(self):
        return list(self._objetos)

    def listar_id(self, id):
        for obj in self._objetos:
            if obj.get_id() == id:
                return obj
        return None

    def atualizar(self, obj):
        atual = self.listar_id(obj.get_id())
        if atual is not None:
            indice = self._objetos.index(atual)
            self._objetos[indice] = obj
            self.salvar()

    def excluir(self, id):
        obj = self.listar_id(id)
        if obj is not None:
            self._objetos.remove(obj)
            self.salvar()
