from datetime import datetime

class paciente:
    def __init__(self, nome, cpf, telefone, nascimento):
        self.__nome = nome
        self.__cpf = cpf
        self.__telefone = telefone
        self.__nascimento = nascimento
    def __str__(self):
        return f"{self.__nome} - {self.__cpf} - {self.__telefone} - {self.__nascimento.strftime('%d/%m/%y')}"
    def idade(self):
        x = datetime.now() - self.__nascimento
        dias = x.days
        anos = dias // 365
        meses = dias % 365 // 30
        return f"{anos} ano(s) e {meses} mês(es)"

x = paciente("nome", "cpf", "telefone", datetime(2010, 12, 20))
print(x)
print(x.idade())