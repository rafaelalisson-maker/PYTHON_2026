import streamlit as st
import pandas as pd
import time

from projeto.models.service import Service


class ManterClienteUI:

    def main():
        st.header("Cadastro de Clientes")

        tab1, tab2, tab3, tab4 = st.tabs(
            ["Listar", "Inserir", "Atualizar", "Excluir"]
        )

        with tab1:
            ManterClienteUI.listar()

        with tab2:
            ManterClienteUI.inserir()

        with tab3:
            ManterClienteUI.atualizar()

        with tab4:
            ManterClienteUI.excluir()

    def listar():
        clientes = Service.cliente_listar()

        if len(clientes) == 0:
            st.write("Nenhum cliente cadastrado")
        else:
            lista_dict = []

            for obj in clientes:
                lista_dict.append(obj.to_json())

            df = pd.DataFrame(lista_dict)
            st.dataframe(df)

    def inserir():
        nome = st.text_input("Informe o nome")
        email = st.text_input("Informe o e-mail")
        fone = st.text_input("Informe o fone")

        if st.button("Inserir"):
            Service.cliente_inserir(nome, email, fone)

            st.success("Cliente inserido com sucesso")

            time.sleep(2)
            st.rerun()

    def atualizar():
        clientes = Service.cliente_listar()

        if len(clientes) == 0:
            st.write("Nenhum cliente cadastrado")
        else:
            op = st.selectbox(
                "Atualização de Clientes",
                clientes
            )

            nome = st.text_input(
                "Novo nome",
                op.get_nome()
            )

            email = st.text_input(
                "Novo e-mail",
                op.get_email()
            )

            fone = st.text_input(
                "Novo fone",
                op.get_fone()
            )

            if st.button("Atualizar"):
                cliente_id = op.get_id()

                Service.cliente_atualizar(
                    cliente_id,
                    nome,
                    email,
                    fone
                )

                st.success("Cliente atualizado com sucesso")

    def excluir():
        clientes = Service.cliente_listar()

        if len(clientes) == 0:
            st.write("Nenhum cliente cadastrado")
        else:
            op = st.selectbox(
                "Exclusão de Clientes",
                clientes
            )

            if st.button("Excluir"):
                cliente_id = op.get_id()

                Service.cliente_excluir(cliente_id)

                st.success("Cliente excluído com sucesso")