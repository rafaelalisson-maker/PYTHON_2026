import pandas as pd
import streamlit as st
from service import Service

class ListarAgendaProfissionalUI:
    @staticmethod
    def main():
        st.header("Agenda do Profissional")

        profissionais = Service.profissional_listar()
        if not profissionais:
            st.info("Nenhum profissional cadastrado.")
            return

        profissional = st.selectbox(
            "Selecione o profissional",
            profissionais,
            format_func=lambda item: item.get_nome(),
        )
        horarios = Service.horario_listar_agenda_profissional(
            profissional.get_id()
        )

        if not horarios:
            st.info("Nenhum horário cadastrado para este profissional.")
            return

        dados = []
        for horario in horarios:
            cliente = Service.cliente_listar_id(horario.get_id_cliente())
            servico = Service.servico_listar_id(horario.get_id_servico())

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
                ),
            })
        st.dataframe(pd.DataFrame(dados), hide_index=True)