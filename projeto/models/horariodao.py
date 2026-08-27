import json

from models.horario import Horario


class HorarioDAO:
    def __init__(self):
        self.__arquivo = "horarios.json"
        self.__objetos = []
        self.__abrir()

    def inserir(self, obj):
        proximo_id = max((item.get_id() for item in self.__objetos), default=0) + 1
        obj.set_id(proximo_id)
        self.__objetos.append(obj)
        self.__salvar()

    def listar(self):
        return self.__objetos

    def listar_id(self, id):
        return next((obj for obj in self.__objetos if obj.get_id() == id), None)

    def atualizar(self, obj):
        indice = next(
            (i for i, atual in enumerate(self.__objetos) if atual.get_id() == obj.get_id()),
            None,
        )
        if indice is not None:
            self.__objetos[indice] = obj
            self.__salvar()

    def excluir(self, id):
        obj = self.listar_id(id)
        if obj is not None:
            self.__objetos.remove(obj)
            self.__salvar()

    def __abrir(self):
        try:
            with open(self.__arquivo, mode="r", encoding="utf-8") as arquivo:
                lista = json.load(arquivo)
        except (FileNotFoundError, json.JSONDecodeError):
            return

        self.__objetos = [Horario.from_json(dicionario) for dicionario in lista]

    def __salvar(self):
        with open(self.__arquivo, mode="w", encoding="utf-8") as arquivo:
            json.dump(
                [obj.to_json() for obj in self.__objetos],
                arquivo,
                ensure_ascii=False,
                indent=2,
            )