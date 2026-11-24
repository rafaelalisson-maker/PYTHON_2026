import sqlite3
from contextlib import closing
from dao_sql.dao import DAO
from models.cliente import Cliente

class ClienteDAO(DAO):
    tabela = "cliente"
    colunas = ("nome", "email", "fone", "senha", "foto")

    def __init__(self):
        pass

    @classmethod
    def abrir(cls):
        cls._garantir_coluna_foto()
        super().abrir()

    @classmethod
    def _garantir_coluna_foto(cls):
        with closing(sqlite3.connect(cls.nome_bd, timeout=30)) as conn:
            with conn:
                colunas = {
                    linha[1]
                    for linha in conn.execute(
                        "PRAGMA table_info(cliente)"
                    ).fetchall()
                }
                if "foto" in colunas:
                    return

                conn.execute("BEGIN IMMEDIATE")
                colunas = {
                    linha[1]
                    for linha in conn.execute(
                        "PRAGMA table_info(cliente)"
                    ).fetchall()
                }
                if "foto" not in colunas:
                    conn.execute(
                        "ALTER TABLE cliente ADD COLUMN foto TEXT"
                    )

    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        try:
            sql = """
                INSERT INTO cliente (nome, email, fone, senha, foto)
                VALUES (?, ?, ?, ?, ?)
            """
            cursor = cls.execute(
                sql,
                (
                    obj.get_nome(),
                    obj.get_email(),
                    obj.get_fone(),
                    obj.get_senha(),
                    obj.to_json()["foto"],
                ),
            )
            obj.set_id(cursor.lastrowid)
        finally:
            cls.fechar()

    @classmethod
    def listar(cls):
        cls.abrir()
        try:
            cursor = cls.execute(
                "SELECT id, nome, email, fone, senha, foto FROM cliente"
            )
            rows = cursor.fetchall()
            return [cls._objeto_da_linha(row) for row in rows]
        finally:
            cls.fechar()

    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        try:
            sql = (
                "SELECT id, nome, email, fone, senha, foto "
                "FROM cliente WHERE id = ?"
            )
            cursor = cls.execute(sql, (id,))
            row = cursor.fetchone()
            return cls._objeto_da_linha(row) if row else None
        finally:
            cls.fechar()

    @classmethod
    def atualizar(cls, obj):
        cls.abrir()
        try:
            sql = """
                UPDATE cliente SET nome=?, email=?, fone=?, senha=?, foto=?
                WHERE id=?
            """
            cls.execute(
                sql,
                (
                    obj.get_nome(),
                    obj.get_email(),
                    obj.get_fone(),
                    obj.get_senha(),
                    obj.to_json()["foto"],
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

    @classmethod
    def _objeto_da_linha(cls, linha):
        dados = dict(zip(("id", *cls.colunas), linha))
        return Cliente.from_json(dados)