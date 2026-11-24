import streamlit as st
import pandas as pd
import time
from service import Service

class ManterProfissionalUI:
    def main():
        st.header("Cadastro de Profissionais")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterProfissionalUI.listar()
        with tab2: ManterProfissionalUI.inserir()
        with tab3: ManterProfissionalUI.atualizar()
        with tab4: ManterProfissionalUI.excluir()

    def listar():
        profissionais = Service.profissional_listar()
        if len(profissionais) == 0: st.write("Nenhum profissional cadastrado")
        else:
            list_dic = []
            for obj in profissionais: list_dic.append(obj.to_dict())
            df = pd.DataFrame(list_dic)
            st.dataframe(df)

    def inserir():
        nome = st.text_input("Informe o nome")
        email = st.text_input("Informe o e-mail")
        especialidade = st.text_input("Informe a especialidade")
        senha = st.text_input("Informe a senha", type="password")
        arquivo_foto = st.file_uploader(
            "Foto do profissional",
            type=["jpg", "jpeg", "png", "webp"],
            key="novo_profissional_foto",
        )
        if st.button("Inserir"):
            try:
                foto = arquivo_foto.getvalue() if arquivo_foto else None
                Service.profissional_inserir(
                    nome, email, especialidade, senha, foto
                )
            except ValueError as exc:
                st.error(str(exc))
            else:
                st.success("Profissional inserido com sucesso")
                time.sleep(2)
                st.rerun()

    def atualizar():
        profissionais = Service.profissional_listar()
        if len(profissionais) == 0: st.write("Nenhum profissional cadastrado")
        else:
            op = st.selectbox("Atualização de Profissionais", profissionais)
            nome = st.text_input("Informe o novo nome", op.get_nome())
            email = st.text_input("Informe o novo email", op.get_email())
            especialidade = st.text_input("Informe a nova especialidade", op.get_especialidade())
            senha = st.text_input("Nova senha", op.get_senha(), type="password")
            if op.get_foto():
                st.image(op.get_foto(), width=150)
            arquivo_foto = st.file_uploader(
                "Nova foto do profissional",
                type=["jpg", "jpeg", "png", "webp"],
                key=f"profissional_foto_{op.get_id()}",
            )

            if st.button("Atualizar"):
                id = op.get_id()
                try:
                    Service.profissional_atualizar(
                        id,
                        nome,
                        email,
                        especialidade,
                        senha,
                        arquivo_foto.getvalue() if arquivo_foto else None,
                    )
                except ValueError as exc:
                    st.error(str(exc))
                else:
                    st.success("Profissional atualizado com sucesso")
                    time.sleep(2)
                    st.rerun()

    def excluir():
        profissionais = Service.profissional_listar()
        if len(profissionais) == 0: st.write("Nenhum profissional cadastrado")
        else:
            op = st.selectbox("Exclusão de Profissionais", profissionais)
            if st.button("Excluir"):
                id = op.get_id()
                try:
                    Service.profissional_excluir(id)
                except ValueError as exc:
                    st.error(str(exc))
                else:
                    st.success("Profissional excluído com sucesso")
                    time.sleep(2)
                    st.rerun()