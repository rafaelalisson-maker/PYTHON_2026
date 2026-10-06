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
        
        if st.button("Inserir"):
            if not nome or not email or not senha:
                st.error("Preencha todos os campos obrigatórios.")
            else:
                Service.cliente_inserir(nome, email, fone, senha)
                st.success("Conta criada com sucesso!")
                time.sleep(2)
                st.rerun()

# Chamada para execução da interface
if __name__ == "__main__":
    AbrirContaUI.main()