import streamlit as st
import time
from service import Service


class AbrirMinhaAgendaUI:

    @staticmethod
    def main():
        st.header("Abrir Minha Agenda")

        data = st.text_input(
            "Informe a data no formato dd/mm/aaaa",
            key="agenda_data"
        )

        horario_inicio = st.text_input(
            "Informe o horário inicial no formato HH:MM",
            key="agenda_inicio"
        )

        horario_fim = st.text_input(
            "Informe o horário final no formato HH:MM",
            key="agenda_fim"
        )

        intervalo = st.number_input(
            "Informe o intervalo entre os horários (min)",
            min_value=1,
            value=30,
            step=5,
            key="agenda_intervalo"
        )

        if st.button("Abrir Agenda"):
            if not data or not horario_inicio or not horario_fim:
                st.warning("Preencha todos os campos.")
                return

            if "usuario_id" not in st.session_state:
                st.error("Faça login antes de abrir a agenda.")
                return

            try:
                quantidade = Service.horario_abrir_minha_agenda(
                    data,
                    horario_inicio,
                    horario_fim,
                    int(intervalo),
                    st.session_state["usuario_id"]
                )

                st.success(
                    f"{quantidade} horário(s) criado(s) com sucesso!"
                )
                time.sleep(1)
                st.rerun()

            except (ValueError, TypeError) as erro:
                st.error(str(erro))