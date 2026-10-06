from projeto.templates.manterclienteUI import ManterClienteUI
from projeto.templates.manterserviceUI import ManterServicoUI
from projeto.templates.manterhorarioUI import ManterHorarioUI
from projeto.templates.manterprofissionalUI import ManterProfissionalUI
from projeto.templates.manteratendimentoUI import ManterAtendimentoUI
from projeto.templates.abrircontaUI import AbrirContaUI
from projeto.templates.loginUI import LoginUI
from projeto.templates.perfilclientesUI import PerfilClienteUI
from projeto.templates.perfilprofissionalUI import PerfilProfissionalUI
from projeto.templates.agendarservicoUI import AgendarServicoUI
from projeto.templates.abrirminhaagendaUI import AbrirMinhaAgendaUI

from projeto.models.service import Service

import streamlit as st


class IndexUI:

    def menu_visitante():
        op = st.sidebar.selectbox(
            "Menu",
            ["Entrar no Sistema", "Abrir Conta"]
        )

        if op == "Entrar no Sistema":
            LoginUI.main()

        if op == "Abrir Conta":
            AbrirContaUI.main()

    def menu_cliente():
        op = st.sidebar.selectbox(
            "Menu",
            ["Meus Dados", "Agendar Serviço"]
        )

        if op == "Meus Dados":
            PerfilClienteUI.main()

        if op == "Agendar Serviço":
            AgendarServicoUI.main()

    def menu_profissional():
        op = st.sidebar.selectbox(
            "Menu",
            ["Meus Dados", "Abrir Minha Agenda"]
        )

        if op == "Meus Dados":
            PerfilProfissionalUI.main()

        if op == "Abrir Minha Agenda":
            AbrirMinhaAgendaUI.main()

    def menu_admin():
        op = st.sidebar.selectbox(
            "Menu",
            [
                "Clientes",
                "Serviços",
                "Horários",
                "Profissionais",
                "Atendimentos"
            ]
        )

        if op == "Clientes":
            ManterClienteUI.main()

        if op == "Serviços":
            ManterServicoUI.main()

        if op == "Horários":
            ManterHorarioUI.main()

        if op == "Profissionais":
            ManterProfissionalUI.main()

        if op == "Atendimentos":
            ManterAtendimentoUI.main()

    def sair_do_sistema():
        if st.sidebar.button("Sair"):
            del st.session_state["usuario_id"]
            del st.session_state["usuario_nome"]
            st.rerun()

    def sidebar():
        if "usuario_id" not in st.session_state:
            IndexUI.menu_visitante()

        else:
            admin = st.session_state["usuario_nome"] == "admin"

            st.sidebar.write(
                "Bem-vindo(a), " +
                st.session_state["usuario_nome"]
            )

            if admin:
                IndexUI.menu_admin()

            else:
                if st.session_state["usuario_tipo"] == "cliente":
                    IndexUI.menu_cliente()

                else:
                    IndexUI.menu_profissional()

            IndexUI.sair_do_sistema()

    def main():
        # Verifica se existe o usuário admin
        Service.cliente_criar_admin()

        # Monta o sidebar
        IndexUI.sidebar()


IndexUI.main()