from dao_sql.dao import DAO
from models.cliente import Cliente

class ClienteDAO(DAO):
    tabela = "cliente"
    colunas = ("nome", "email", "fone", "senha")

    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        try:
            sql = """
                INSERT INTO cliente (nome, email, fone, senha)
                VALUES (?, ?, ?, ?)
            """
            cursor = cls.execute(
                sql,
                (
                    obj.get_nome(),
                    obj.get_email(),
                    obj.get_fone(),
                    obj.get_senha(),
                ),
            )
            obj.set_id(cursor.lastrowid)
        finally:
            cls.fechar()

    @classmethod
    def listar(cls):
        cls.abrir()
        try:
            cursor = cls.execute("SELECT * FROM cliente")
            rows = cursor.fetchall()
            return [
                Cliente(id, nome, email, fone, senha)
                for id, nome, email, fone, senha in rows
            ]
        finally:
            cls.fechar()

    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        try:
            sql = "SELECT * FROM cliente WHERE id = ?"
            cursor = cls.execute(sql, (id,))
            row = cursor.fetchone()
            return Cliente(*row) if row else None
        finally:
            cls.fechar()

    @classmethod
    def atualizar(cls, obj):
        cls.abrir()
        try:
            sql = """
                UPDATE cliente SET nome=?, email=?, fone=?, senha=?
                WHERE id=?
            """
            cls.execute(
                sql,
                (
                    obj.get_nome(),
                    obj.get_email(),
                    obj.get_fone(),
                    obj.get_senha(),
                    obj.get_id(),
                ),
            )
        finally:
            cls.fechar()

    @classmethod
    def excluir(cls, obj):
        cls.abrir()
        try:
            sql = "DELETE FROM cliente WHERE id=?"
            cls.execute(sql, (obj,))
        finally:
            cls.fechar()

    def _objeto_da_linha(self, linha):
        return Cliente.from_json(linha)