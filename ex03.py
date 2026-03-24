class triangulo:
    def __init__(self):
        self.b = 0        #atributo
        self.h = 0
    def calc_area (self): #método
        return self.b * self.h / 2 
    
x = [1, 2, 3]
y = x
y.append(4)
print (x)
print (type(x), type(y))

# x é euma referencia - alguem que armazena o enderoco de um objeto
# triangulo() cria um objeto ou instancia da classe
x = triangulo()
print (x)
y = x
print (y)