class Musica:
    def __init__(self, id, t, art, alb):
        self.__id = id
        self.__titulo = t
        self.__artista = art
        self.__album = alb

    def get_id(self): return self.__id
    def set_id(self, id): self.__id = id
    def get_titulo(self): return self.__titulo
    def set_titulo(self, t): self.__titulo = t
    def get_artista(self): return self.__artista
    def set_artista(self, art): self.__artista = art
    def get_album(self): return self.__album
    def set_album(self, alb): self.__album = alb

    def ToString(self):
        return f"ID: {self.__id} | Música: {self.__titulo} | Artista: {self.__artista} | Álbum: {self.__album}"

class PlayList:
    def __init__(self, id, n, d):
        self.__id = id
        self.__nome = n
        self.__descricao = d

    def get_id(self): return self.__id
    def set_id(self, id): self.__id = id
    def get_nome(self): return self.__nome
    def set_nome(self, n): self.__nome = n
    def get_descricao(self): return self.__descricao
    def set_descricao(self, d): self.__descricao = d

    def ToString(self):
        return f"ID: {self.__id} | Playlist: {self.__nome} | Descrição: {self.__descricao}"

class PlayListItem:
    def __init__(self, id, ip, im, s):
        self.__id = id
        self.__idPlayList = ip
        self.__idMusica = im
        self.__sequencia = s

    def get_id(self): return self.__id
    def set_id(self, id): self.__id = id
    def get_idPlayList(self): return self.__idPlayList
    def set_idPlayList(self, ip): self.__idPlayList = ip
    def get_idMusica(self): return self.__idMusica
    def set_idMusica(self, im): self.__idMusica = im
    def get_sequencia(self): return self.__sequencia
    def set_sequencia(self, s): self.__sequencia = s

    def ToString(self):
        return f"Item ID: {self.__id} | Playlist ID: {self.__idPlayList} | Música ID: {self.__idMusica} | Seq: {self.__sequencia}"

class UI:
    playlists = []
    musicas = []
    itens = []

    @classmethod
    def Main(cls):
        while True:
            print("\n--- MENU PLAYLIST ---")
            print("1- Inserir Playlist | 2- Listar | 3- Atualizar | 4- Excluir")
            print("5- Inserir Música   | 6- Listar | 7- Atualizar | 8- Excluir")
            print("9- Adicionar Música na Playlist (Item)")
            print("10- Listar Itens de Playlists")
            print("0- Sair")
            op = input("Escolha: ")

            if op == "1": cls.inserir_playlist()
            elif op == "2": cls.listar_playlists()
            elif op == "5": cls.inserir_musica()
            elif op == "6": cls.listar_musicas()
            elif op == "9": cls.inserir_item()
            elif op == "10": cls.listar_itens()
            elif op == "0": break

    @classmethod
    def inserir_playlist(cls):
        id = int(input("ID: "))
        nome = input("Nome: ")
        desc = input("Descrição: ")
        cls.playlists.append(PlayList(id, nome, desc))

    @classmethod
    def listar_playlists(cls):
        for p in cls.playlists: print(p.ToString())

    @classmethod
    def inserir_musica(cls):
        id = int(input("ID: "))
        titulo = input("Título: ")
        artista = input("Artista: ")
        album = input("Álbum: ")
        cls.musicas.append(Musica(id, titulo, artista, album))

    @classmethod
    def listar_musicas(cls):
        for m in cls.musicas: print(m.ToString())

    @classmethod
    def inserir_item(cls):
        id = int(input("ID do Item: "))
        id_p = int(input("ID da Playlist: "))
        id_m = int(input("ID da Música: "))
        seq = int(input("Sequência: "))
        cls.itens.append(PlayListItem(id, id_p, id_m, seq))

    @classmethod
    def listar_itens(cls):
        for i in cls.itens: print(i.ToString())

if __name__ == "__main__":
    UI.Main()