class cliente:
    def __init__(self, id, nome, email, fone):
        self.set_id (id)
        self.set_nome (nome)
        self.set_email (email)
        self.set_fone (fone)

    def __str__(self):
        return f"{self.__id} - {self.__nome} - {self.__email} - {self.__fome}"
    
    def set_id(self, id):
        if id < 0: raise ValueError("Id deve ser positivo")
        self.__id = id
    def set_nome(self, nome):
        if nome == "": raise ValueError("Nome deve ser informado")
        self.__nome = nome
    def set_email(self, email):
        if  email == "": raise ValueError("E-mail deve ser informado")
        self.__email = email
    def set_fone(self, fone):
        if fone == "": raise ValueError("fone deve ser informado")
        self.__fone = fone