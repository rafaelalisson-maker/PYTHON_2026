from enum import Enum
from datetime import datetime


class Pagamento(Enum):
    EM_ABERTO = 1
    PAGO_PARCIAL = 2
    PAGO = 3


class Boleto:
    def __init__(self, cod, emissao, venc, valor):
        self.set_cod_barras(cod)
        self.set_data_emissao(emissao)
        self.set_data_vencimento(venc)
        self.set_valor_boleto(valor)

        self.__data_pagamento = None
        self.__valor_pago = 0
        self.__situacao_pagamento = Pagamento.EM_ABERTO

    def set_cod_barras(self, cod):
        if len(cod) != 10 or not cod.isdigit():
            raise ValueError("Código deve possuir exatamente 10 dígitos")
        self.__cod_barras = cod

    def set_data_emissao(self, emissao):
        if emissao > datetime.now():
            raise ValueError("Data de emissão não pode ser futura")
        self.__data_emissao = emissao

    def set_data_vencimento(self, venc):
        self.__data_vencimento = venc

    def set_valor_boleto(self, valor):
        if valor <= 0:
            raise ValueError("Valor do boleto deve ser positivo")
        self.__valor_boleto = valor

    def pagar(self, valor_pago):
        if valor_pago <= 0:
            raise ValueError("Valor pago deve ser positivo")

        if self.__situacao_pagamento != Pagamento.EM_ABERTO:
            raise ValueError("Boleto já foi pago")

        if valor_pago > self.__valor_boleto:
            raise ValueError("Valor pago maior que o valor do boleto")

        self.__valor_pago = valor_pago
        self.__data_pagamento = datetime.now()

        if valor_pago == self.__valor_boleto:
            self.__situacao_pagamento = Pagamento.PAGO
        else:
            self.__situacao_pagamento = Pagamento.PAGO_PARCIAL

    def get_cod_barras(self):
        return self.__cod_barras

    def get_data_emissao(self):
        return self.__data_emissao

    def get_data_vencimento(self):
        return self.__data_vencimento

    def get_valor_boleto(self):
        return self.__valor_boleto

    def get_valor_pago(self):
        return self.__valor_pago

    def get_data_pagamento(self):
        return self.__data_pagamento

    def get_situacao_pagamento(self):
        return self.__situacao_pagamento

    def __str__(self):
        texto = (
            f"\nCódigo: {self.__cod_barras}\n"
            f"Emissão: {self.__data_emissao.strftime('%d/%m/%Y')}\n"
            f"Vencimento: {self.__data_vencimento.strftime('%d/%m/%Y')}\n"
            f"Valor: R$ {self.__valor_boleto:.2f}\n"
            f"Valor Pago: R$ {self.__valor_pago:.2f}\n"
        )

        if self.__data_pagamento:
            texto += (
                f"Pagamento: "
                f"{self.__data_pagamento.strftime('%d/%m/%Y')}\n"
            )

        texto += f"Situação: {self.__situacao_pagamento.name}"

        return texto


class BoletoUI:
    __boletos = []

    @staticmethod
    def main():
        op = 0
        while op != 10:
            op = BoletoUI.menu()

            if op == 1:
                BoletoUI.inserir()
            elif op == 2:
                BoletoUI.listar()
            elif op == 3:
                BoletoUI.atualizar()
            elif op == 4:
                BoletoUI.excluir()
            elif op == 5:
                BoletoUI.boletos_em_aberto()
            elif op == 6:
                BoletoUI.boletos_pagos()
            elif op == 7:
                BoletoUI.boletos_a_vencer()
            elif op == 8:
                BoletoUI.vencidos()
            elif op == 9:
                BoletoUI.pagar_boleto()

    @staticmethod
    def menu():
        print("---------------------------------------------")
        print(" 1-Inserir, 2-Listar, 3-Atualizar, 4-Excluir ")
        print(" 5-Boletos em Aberto, 6-Boletos Pagos        ")
        print(" 7-Boletos a Vencer,  8-Boletos Vencidos     ")
        print(" 9-Pagar Boletos,     10-Fim                 ")
        print("---------------------------------------------")
        return int(input("Escolha uma opção: "))

    @classmethod
    def inserir(cls):
        cod = input("Informe o código do boleto com 10 dígitos: ")
        emissao = datetime.strptime(
            input("Informe a data de emissão dd/mm/aaaa: "),
            "%d/%m/%Y"
        )
        venc = datetime.strptime(
            input("Informe a data de vencimento dd/mm/aaaa: "),
            "%d/%m/%Y"
        )
        valor = float(input("Informe o valor: "))

        cls.__boletos.append(Boleto(cod, emissao, venc, valor))

    @classmethod
    def listar(cls):
        for b in cls.__boletos:
            print(b)
            print("-" * 40)

    @classmethod
    def atualizar(cls):
        cod = input("Código do boleto a atualizar: ")

        for i, b in enumerate(cls.__boletos):
            if b.get_cod_barras() == cod:

                emissao = datetime.strptime(
                    input("Nova data de emissão (dd/mm/aaaa): "),
                    "%d/%m/%Y"
                )

                venc = datetime.strptime(
                    input("Nova data de vencimento (dd/mm/aaaa): "),
                    "%d/%m/%Y"
                )

                valor = float(input("Novo valor: "))

                cls.__boletos[i] = Boleto(cod, emissao, venc, valor)
                print("Boleto atualizado.")
                return

        print("Boleto não encontrado.")

    @classmethod
    def excluir(cls):
        cod = input("Código do boleto a excluir: ")

        for b in cls.__boletos:
            if b.get_cod_barras() == cod:
                cls.__boletos.remove(b)
                print("Boleto removido.")
                return

        print("Boleto não encontrado.")

    @classmethod
    def boletos_em_aberto(cls):
        for b in cls.__boletos:
            if b.get_situacao_pagamento() == Pagamento.EM_ABERTO:
                print(b)
                print("-" * 40)

    @classmethod
    def boletos_pagos(cls):
        for b in cls.__boletos:
            if b.get_situacao_pagamento() in (
                Pagamento.PAGO,
                Pagamento.PAGO_PARCIAL
            ):
                print(b)
                print("-" * 40)

    @classmethod
    def boletos_a_vencer(cls):
        hoje = datetime.now()

        for b in cls.__boletos:
            if (b.get_situacao_pagamento() == Pagamento.EM_ABERTO and
                    b.get_data_vencimento() >= hoje):
                print(b)
                print("-" * 40)

    @classmethod
    def vencidos(cls):
        hoje = datetime.now()

        for b in cls.__boletos:
            if (b.get_situacao_pagamento() == Pagamento.EM_ABERTO and
                    b.get_data_vencimento() < hoje):
                print(b)
                print("-" * 40)

    @classmethod
    def pagar_boleto(cls):
        cod = input("Código do boleto: ")

        for b in cls.__boletos:
            if b.get_cod_barras() == cod:
                valor = float(input("Valor pago: "))

                try:
                    b.pagar(valor)
                    print("Pagamento registrado.")
                except Exception as erro:
                    print("Erro:", erro)

                return

        print("Boleto não encontrado.")