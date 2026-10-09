
import streamlit as st
import pandas as pd
from service import Service


class VisualizarMinhaAgendaUI:
    @staticmethod
    def main():
        st.header("Minha Agenda")

        if "usuario_id" not in st.session_state:
            st.warning("Faça login para visualizar sua agenda.")
            return

        horarios = Service.horario_visualizar_minha_agenda(
            st.session_state["usuario_id"]
        )

        if not horarios:
            st.info("Nenhum horário cadastrado.")
            return

        dados = []

        for horario in horarios:
            cliente = Service.cliente_listar_id(
                horario.get_id_cliente()
            )
            servico = Service.servico_listar_id(
                horario.get_id_servico()
            )

            dados.append({
                "ID": horario.get_id(),
                "Data e horário": horario.get_data().strftime(
                    "%d/%m/%Y %H:%M"
                ),
                "Cliente": (
                    cliente.get_nome()
                    if cliente and horario.get_id_cliente() not in [0, None]
                    else "Disponível"
                ),
                "Serviço": (
                    servico.get_descricao()
                    if servico and horario.get_id_servico() not in [0, None]
                    else "Não definido"
                ),
                "Confirmado": (
                    "Sim" if horario.get_confirmado() else "Não"
                )
            })

        st.dataframe(pd.DataFrame(dados), hide_index=True)