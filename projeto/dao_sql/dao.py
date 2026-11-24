import sqlite3
from abc import ABC, abstractmethod

class DAO(ABC):
    conn = None
    nome_bd = "agenda.db"
    tabela = ""
    colunas = ()

    def _abrir_se_necessario(self):
        if DAO.conn is None:
            DAO.abrir()

    @classmethod
    def abrir(cls):
        cls.conn = sqlite3.connect(cls.nome_bd)
        cls.conn.execute("PRAGMA foreign_keys = ON")

    @classmethod
    def execute(cls, sql, params=None):
        cursor = cls.conn.cursor()
        cursor.execute(sql, params or [])
        cls.conn.commit()
        return cursor

    @abstractmethod
    def _objeto_da_linha(self, linha):
        raise NotImplementedError

    def _valores(self, obj):
        dados = obj.to_json()
        return tuple(dados[coluna] for coluna in self.colunas)

    def _dados_da_linha(self, linha):
        return dict(zip(("id", *self.colunas), linha))

    def inserir(self, obj):
        self._abrir_se_necessario()
        marcadores = ", ".join("?" for _ in self.colunas)
        colunas = ", ".join(self.colunas)
        try:
            cursor = DAO.execute(
                f"INSERT INTO {self.tabela} ({colunas}) "
                f"VALUES ({marcadores})",
                self._valores(obj),
            )
        except Exception:
            DAO.conn.rollback()
            raise
        obj.set_id(cursor.lastrowid)

    def listar(self):
        self._abrir_se_necessario()
        linhas = DAO.execute(
            f"SELECT * FROM {self.tabela} ORDER BY id"
        ).fetchall()
        return [
            self._objeto_da_linha(self._dados_da_linha(linha))
            for linha in linhas
        ]

    def listar_id(self, id):
        self._abrir_se_necessario()
        linha = DAO.execute(
            f"SELECT * FROM {self.tabela} WHERE id = ?",
            (id,),
        ).fetchone()
        return (
            self._objeto_da_linha(self._dados_da_linha(linha))
            if linha is not None
            else None
        )

    def atualizar(self, obj):
        self._abrir_se_necessario()
        atribuicoes = ", ".join(
            f"{coluna} = ?" for coluna in self.colunas
        )
        try:
            DAO.execute(
                f"UPDATE {self.tabela} SET {atribuicoes} WHERE id = ?",
                (*self._valores(obj), obj.get_id()),
            )
        except Exception:
            DAO.conn.rollback()
            raise

    def excluir(self, id):
        self._abrir_se_necessario()
        try:
            DAO.execute(
                f"DELETE FROM {self.tabela} WHERE id = ?",
                (id,),
            )
        except Exception:
            DAO.conn.rollback()
            raise

    @classmethod
    def fechar(cls):
        if cls.conn is not None:
            cls.conn.close()
            cls.conn = None