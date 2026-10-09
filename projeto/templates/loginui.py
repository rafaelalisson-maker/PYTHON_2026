import streamlit as st
from service import Service


class LoginUI:

    @staticmethod
    def main():
        st.header("Entrar no Sistema")
        email = st.text_input("Informe o e-mail")
        senha = st.text_input("Informe a senha", type="password")

        if st.button("Entrar"):
            # Autenticação de Cliente / Admin
            c = Service.cliente_autenticar(email, senha)
            if c is not None:
                # Suporta retorno por Dicionário ou Objeto
                c_id = c["id"] if isinstance(c, dict) else c.get_id()
                c_nome = c["nome"] if isinstance(c, dict) else c.get_nome()

                st.session_state["usuario_id"] = c_id
                st.session_state["usuario_nome"] = c_nome
                st.session_state["usuario_tipo"] = "cliente"
                st.rerun()

            # Autenticação de Profissional
            p = Service.profissional_autenticar(email, senha)
            if p is not None:
                p_id = p["id"] if isinstance(p, dict) else p.get_id()
                p_nome = p["nome"] if isinstance(p, dict) else p.get_nome()

                st.session_state["usuario_id"] = p_id
                st.session_state["usuario_nome"] = p_nome
                st.session_state["usuario_tipo"] = "profissional"
                st.rerun()

            # Se nenhum dos dois autenticou
            if c is None and p is None:
                st.error("E-mail ou senha inválidos")