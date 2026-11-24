import streamlit as st
import time
from service import Service

class AbrirContaUI:
    @staticmethod
    def main():
        st.header("Abrir Conta no Sistema")
        nome = st.text_input("Informe o nome")
        email = st.text_input("Informe o e-mail")
        fone = st.text_input("Informe o fone")
        senha = st.text_input("Informe a senha", type="password")
        arquivo_foto = st.file_uploader(
            "Foto do cliente",
            type=["jpg", "jpeg", "png", "webp"],
            key="nova_conta_foto",
        )
        
        if st.button("Inserir"):
            if not nome or not email or not senha:
                st.error("Preencha todos os campos obrigatórios.")
            else:
                try:
                    foto = arquivo_foto.getvalue() if arquivo_foto else None
                    Service.cliente_inserir(nome, email, fone, senha, foto)
                except ValueError as exc:
                    st.error(str(exc))
                else:
                    st.success("Conta criada com sucesso!")
                    time.sleep(2)
                    st.rerun()

if __name__ == "__main__":
    AbrirContaUI.main()