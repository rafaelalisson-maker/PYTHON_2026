from Service import Service
class UI:

    @staticmethod
    def menu():
        op = -1

        while op != 0:
            print("\n=== SISTEMA DE CLIENTES ===")
            print("1 - Inserir cliente")
            print("2 - Listar clientes")
            print("3 - Pesquisar cliente por nome")
            print("4 - Atualizar cliente")
            print("5 - Excluir cliente")
            print("0 - Sair")

            op = int(input("Opção: "))

            if op == 1:
                UI.cliente_inserir()

            elif op == 2:
                UI.cliente_listar()

            elif op == 3:
                UI.cliente_pesquisar_nome()

            elif op == 4:
                UI.cliente_atualizar()

            elif op == 5:
                UI.cliente_excluir()

    @staticmethod
    def cliente_inserir():
        print("\n=== Inserir Cliente ===")
        nome = input("Nome: ")
        email = input("E-mail: ")
        fone = input("Telefone: ")

        Service.cliente_inserir(nome, email, fone)
        print("Cliente cadastrado com sucesso!")

    @staticmethod
    def cliente_listar():
        print("\n=== Lista de Clientes ===")
        for cliente in Service.cliente_listar():
            print(cliente)

    @staticmethod
    def cliente_pesquisar_nome():
        nome = input("Digite o início do nome: ")

        clientes = Service.cliente_listar_nome(nome)

        if len(clientes) == 0:
            print("Nenhum cliente encontrado.")
        else:
            for cliente in clientes:
                print(cliente)

    @staticmethod
    def cliente_atualizar():
        id = int(input("ID: "))
        nome = input("Nome: ")
        email = input("E-mail: ")
        fone = input("Telefone: ")

        Service.cliente_atualizar(id, nome, email, fone)
        print("Cliente atualizado!")

    @staticmethod
    def cliente_excluir():
        id = int(input("ID: "))
        Service.cliente_excluir(id)
        print("Cliente excluído!")

UI.menu()