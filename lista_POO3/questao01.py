class retangulo:
    def __init__ (self, b , h):
        if b <= 0 or h <=0:
            raise ValueError("base e altura devem ser positivas")
        self.b = b
        self.h = h
    
    def setBase(self, b):
        if b > 0:
            self.b = b
    def setAltura(self, h):
        if h > 0:
            self.h = h
    
    def getBase (self):
        return self.b
    
    def getAltura (self):
        return self.h
    
    def calcArea (self):
        self.setBase * self.setAltura
    
    def calcDiagonal (self):
        return (self.b ** 2 + self.h ** 2)
    
    def __str__ (self):
        return  