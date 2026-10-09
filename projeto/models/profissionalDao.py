import json
from models.profissional import Profissional


class profissionalDao:
    def __init__(self):
        self.__arquivo = "profissionais.json"
        self.__objetos = []
        self.__abrir()

    def inserir(self, obj):
        maior_id = max(
            (profissional.get_id() for profissional in self.__objetos),
            default=0
        )
        obj.set_id(maior_id + 1)
        self.__objetos.append(obj)
        self.__salvar()

    def listar(self):
        return list(self.__objetos)

    def listar_id(self, id):
        for obj in self.__objetos:
            if obj.get_id() == id:
                return obj
        return None

    def atualizar(self, obj):
        atual = self.listar_id(obj.get_id())
        if atual is not None:
            indice = self.__objetos.index(atual)
            self.__objetos[indice] = obj
            self.__salvar()

    def excluir(self, id):
        obj = self.listar_id(id)
        if obj is not None:
            self.__objetos.remove(obj)
            self.__salvar()

    def __abrir(self):
        try:
            with open(self.__arquivo, "r", encoding="utf-8") as arquivo:
                lista = json.load(arquivo)

            self.__objetos = [
                Profissional.from_json(dicionario)
                for dicionario in lista
            ]
        except (FileNotFoundError, json.JSONDecodeError):
            self.__objetos = []

    def __salvar(self):
        with open(self.__arquivo, "w", encoding="utf-8") as arquivo:
            json.dump(
                [obj.to_json() for obj in self.__objetos],
                arquivo,
                ensure_ascii=False,
                indent=2
            )