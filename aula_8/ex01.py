import json
class cliente:
    def __init__(self, id, nome):
        self.id = id
        self.mome = nome
    def __str__(slef):
        return f"{self.id} - {self.nome}"
    def to_json(self):
        return {"id" : self.id, "nome" : self.nome }
    @staticmethod
    def from_json(dic):
        cliente(dic["id"], dic["nome"])
    
    a = cliente(1, "Douglas Crockford")
    b = cliente(2, "Jon Rosak")
    c = cliente.from_json({ "id" : 3, "nome" : "Alan Turing" })
    
    lista = [a, b, c] 
    arquivo = open("clientes.json", mode="w")
    json.dump(lista, arquivo, default = cliente.tojson)
    arquivo.close() 
    

    print (a)
    print (b)
    print (a.__dict__)
    print (b.__dict__)
    print (vars(a))
    print (vars(b))
    print(a.to_json())
    print(b.to_json())