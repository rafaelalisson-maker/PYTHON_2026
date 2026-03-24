class triangulo:
    def __init__(self):
        self.b = 0        #atributo
        self.h = 0
    def calc_area (self): #método
        return self.b * self.h / 2    

x = triangulo()
print(x.b, x.h)
x.b = float(input("informe a base do triangulo"))
x.h = float(input("informe a base do triangulo"))
print(x.b, x.h)
a = x.calc_area()
print(f"A area do triangulo é {a:.2f}")

y = triangulo()
print(y.b, y.h)
y.b = float(input("informe a base do segundo triangulo"))
y.h = float(input("informe a base do segundo triangulo"))
print(x.b, x.h)
a = x.calc_area()
print(f"A area do triangulo é {a:.2f}")