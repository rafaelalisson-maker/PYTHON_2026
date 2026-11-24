import streamlit as st
from service import Service
import time

class PerfilClienteUI:
    def main():
        st.header("Meus Dados")
        op = Service.cliente_listar_id(st.session_state["usuario_id"])
        if op is None:
            st.error("Cliente não encontrado.")
            return

        nome = st.text_input("Informe o novo nome", op.get_nome())
        email = st.text_input("Informe o novo e-mail", op.get_email())
        fone = st.text_input("Informe o novo fone", op.get_fone())
        senha = st.text_input("Informe a nova senha", op.get_senha(),type="password")
        if op.get_foto():
            st.image(op.get_foto(), width=150)
        arquivo_foto = st.file_uploader(
            "Nova foto",
            type=["jpg", "jpeg", "png", "webp"],
            key=f"perfil_cliente_foto_{op.get_id()}",
        )
        if st.button("Atualizar"):
            id = op.get_id()
            try:
                Service.cliente_atualizar(
                    id,
                    nome,
                    email,
                    fone,
                    senha,
                    arquivo_foto.getvalue() if arquivo_foto else None,
                )
            except ValueError as exc:
                st.error(str(exc))
            else:
                st.success("Cliente atualizado com sucesso")
                time.sleep(2)
                st.rerun()