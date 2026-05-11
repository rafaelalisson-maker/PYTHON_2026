class Time:
    def __init__(self, id, nome, estado):
        self.__id = id
        self.__nome = nome
        self.__estado = estado

    def get_id(self):
        return self.__id

    def get_nome(self):
        return self.__nome

    def get_estado(self):
        return self.__estado

    def set_nome(self, nome):
        self.__nome = nome

    def set_estado(self, estado):
        self.__estado = estado

    def to_string(self):
        return f"ID: {self.__id} | Nome: {self.__nome} | Estado: {self.__estado}"


class Jogador:
    def __init__(self, id, nome, camisa, id_time):
        self.__id = id
        self.__nome = nome
        self.__camisa = camisa
        self.__id_time = id_time

    def get_id(self):
        return self.__id

    def get_nome(self):
        return self.__nome

    def get_camisa(self):
        return self.__camisa

    def get_id_time(self):
        return self.__id_time

    def set_nome(self, nome):
        self.__nome = nome

    def set_camisa(self, camisa):
        self.__camisa = camisa

    def set_id_time(self, id_time):
        self.__id_time = id_time

    def to_string(self):
        return (
            f"ID: {self.__id} | Nome: {self.__nome} | "
            f"Camisa: {self.__camisa} | Time: {self.__id_time}"
        )

class UI:
    def __init__(self):
        self.times = []
        self.jogadores = []

    def inserir_time(self):
        id = int(input("ID: "))
        nome = input("Nome: ")
        estado = input("Estado: ")

        time = Time(id, nome, estado)
        self.times.append(time)

        print("Time cadastrado!")

    def listar_times(self):
        for t in self.times:
            print(t.to_string())

    def atualizar_time(self):
        id = int(input("ID do time: "))

        for t in self.times:
            if t.get_id() == id:
                nome = input("Novo nome: ")
                estado = input("Novo estado: ")

                t.set_nome(nome)
                t.set_estado(estado)

                print("Time atualizado!")
                return

        print("Time não encontrado.")

    def excluir_time(self):
        id = int(input("ID do time: "))

        for t in self.times:
            if t.get_id() == id:
                self.times.remove(t)
                print("Time removido!")
                return

        print("Time não encontrado.")

    def inserir_jogador(self):
        id = int(input("ID: "))
        nome = input("Nome: ")
        camisa = int(input("Camisa: "))
        id_time = int(input("ID do time: "))

        jogador = Jogador(id, nome, camisa, id_time)
        self.jogadores.append(jogador)
        print("Jogador cadastrado!")

    def listar_jogadores(self):
        for j in self.jogadores:
            print(j.to_string())

    def atualizar_jogador(self):
        id = int(input("ID do jogador: "))

        for j in self.jogadores:
            if j.get_id() == id:
                nome = input("Novo nome: ")
                camisa = int(input("Nova camisa: "))

                j.set_nome(nome)
                j.set_camisa(camisa)

                print("Jogador atualizado!")
                return

        print("Jogador não encontrado.")

    def excluir_jogador(self):
        id = int(input("ID do jogador: "))

        for j in self.jogadores:
            if j.get_id() == id:
                self.jogadores.remove(j)
                print("Jogador removido!")
                return

        print("Jogador não encontrado.")

    def listar_jogadores_do_time(self):
        id_time = int(input("ID do time: "))

        for j in self.jogadores:
            if j.get_id_time() == id_time:
                print(j.to_string())

    def transferir_jogador(self):
        id_jogador = int(input("ID do jogador: "))
        novo_time = int(input("Novo time: "))

        for j in self.jogadores:
            if j.get_id() == id_jogador:
                j.set_id_time(novo_time)
                print("Transferência realizada!")
                return

        print("Jogador não encontrado.")

    def menu(self):
        print("\n1 - Inserir Time")
        print("2 - Listar Times")
        print("3 - Atualizar Time")
        print("4 - Excluir Time")
        print("5 - Inserir Jogador")
        print("6 - Listar Jogadores")
        print("7 - Atualizar Jogador")
        print("8 - Excluir Jogador")
        print("9 - Jogadores do Time")
        print("10 - Transferir Jogador")
        print("0 - Sair")

    def main(self):
        while True:
            self.menu()

            op = int(input("Opção: "))

            if op == 1:
                self.inserir_time()

            elif op == 2:
                self.listar_times()

            elif op == 3:
                self.atualizar_time()

            elif op == 4:
                self.excluir_time()

            elif op == 5:
                self.inserir_jogador()

            elif op == 6:
                self.listar_jogadores()

            elif op == 7:
                self.atualizar_jogador()

            elif op == 8:
                self.excluir_jogador()

            elif op == 9:
                self.listar_jogadores_do_time()

            elif op == 10:
                self.transferir_jogador()

            elif op == 0:
                print("Encerrando...")
                break

            else:
                print("Opção inválida.")


ui = UI()
ui.main()