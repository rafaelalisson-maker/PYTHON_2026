import streamlit as st
from paciente import paciente
from datetime import date

class pacienteUI:
    def main():
        st.header("Dados do Paciente")
        nome = st.text_input("Nome")
        cpf = st.text_input("CPF")
        telefone = st.text_input("Telefone")
        nascimento = st.date_input("Data de Nascimento", value = date(2000, 1, 1))
        if st.button("Cadastrar"):
            p = paciente(nome, cpf, telefone, nascimento)
            st.success("Paciente cadastrado com sucesso!")
            st.write(p)
            st.write("Idade:", p.idade())