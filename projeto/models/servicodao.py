import json
from models.dao import DAO
from models.servico import Servico


class ServicoDAO(DAO):
    def abrir(self):
        try:
            with open("servicos.json", "r", encoding="utf-8") as arquivo:
                lista = json.load(arquivo)
        except (FileNotFoundError, json.JSONDecodeError):
            self._objetos = []
            return

        self._objetos = [
            Servico.from_json(dicionario)
            for dicionario in lista
        ]

    def salvar(self):
        with open("servicos.json", "w", encoding="utf-8") as arquivo:
            json.dump(
                [obj.to_json() for obj in self._objetos],
                arquivo,
                ensure_ascii=False,
                indent=2
            )