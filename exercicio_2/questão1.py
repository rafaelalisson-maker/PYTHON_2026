class agua:
    def _init_(self, agua, mes, consumo):
        self.agua = agua
        self.mes = mes
        self.consumo = consumo
    def calcular_valor(self):
        if self.consumo <= 10:
            return 38.0
        elif self.consumo <= 20:
              excedente = self.consumo - 10
              return 38.0 + (excedente * 5.0)
        else:
            excedente1 = (10 * 5)
            excedende2 = (self.consumo - 20) * 6.0
            return 38.0 + excedente1 + excedente2
        
mes = input ('digite o mes: ')
ano = int (input('digite o ano: '))
consumo = float(input('digite o consumo: '))

conta = agua(mes, ano, consumo)
print = (f'valor da conta: {conta.calcular_valor():.2f}')