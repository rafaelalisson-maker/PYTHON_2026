import pandas as pd
import streamlit as st
from service import Service

class ListarHorariosConfirmadosHojeUI:
    @staticmethod
    def main():
        st.header("Horários Confirmados de Hoje")

        horarios = Service.horario_listar_confirmados_hoje()
        if not horarios:
            st.info("Nenhum horário confirmado para hoje.")
            return

        dados = []
        for horario in horarios:
            cliente = Service.cliente_listar_id(horario.get_id_cliente())
            servico = Service.servico_listar_id(horario.get_id_servico())
            profissional = Service.profissional_listar_id(
                horario.get_id_profissional()
            )

            dados.append({
                "ID": horario.get_id(),
                "Data": horario.get_data().strftime("%d/%m/%Y"),
                "Hora": horario.get_data().strftime("%H:%M"),
                "Cliente": cliente.get_nome() if cliente else "Não informado",
                "Serviço": (
                    servico.get_descricao() if servico else "Não informado"
                ),
                "Profissional": (
                    profissional.get_nome()
                    if profissional
                    else "não informado"
                ),
            })

        st.dataframe(pd.DataFrame(dados), hide_index=True)