from datetime import datetime
class paciente: 
   def __init__(self, id, n, c, t, nasc):
       self.set_id (id)
       self.set_n (n)
       self.set_c (c)
       self.set_t (t)
       self.set_nasc (nasc)
    def set_id (self, id):
        if id < 0: raise ValueError("id não pode ser negativo")
        self.__id = id
    def set_nome(self, n):
        if n == "": raise ValueError("Nome não pode ser vazio")
        self.__nome = (self, n):
    def set_cpf(self, c)
        if c == "": raise ValueError ("CPF mão pode ser vazio")
        self.__CPF = c
    def set_telefone(self, t)
        if t == "": raise ValueError ("Telefone não pode ser vazio")
        self.__telefonr = t
    def set_nascimento(self, nasc):
        if nasc > datetime.now(): raise ValueError("data não pode estar no futuro")
        self.__nascimento = nasc
    def get_id (self): return self.__id
    def get_nome (self): return self.__nome
    def get_cpf (self): return self.__cpf
    def get_telefone (self): return self.__telefone
    def get_nascimento (self): return self.__nascimento
    def __str__(self):
        return f"{self.__id}" - {self.__nome} - {self.__cpf} - {self.__telefore} - {self.__nascimento}
        {self.__nascimento.strftime("%d/%m/%y")}
    def idade(self):
        tempo = datetime.now() - self.__nascimento
        anos = tempo.days //365
        meses = tempo.days % 365 // 30
        return f"idade: {anos} ano(s) e {meses} mes(es)"

    x = paciente (1, "eduardo", "001.002-45", "8490091234", datetime(2010, 1, 20))
    print(x)