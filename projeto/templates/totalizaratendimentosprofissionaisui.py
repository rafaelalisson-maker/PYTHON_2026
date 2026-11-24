from datetime import date

import pandas as pd
import streamlit as st

from service import Service


class TotalizarAtendimentosProfissionaisUI:
    @staticmethod
    def main():
        st.header("Totalizar Atendimentos dos Profissionais")

        data_inicio = st.date_input("Data inicial", value=date.today())
        data_fim = st.date_input("Data final", value=date.today())
        if data_inicio > data_fim:
            st.warning(
                "A data inicial deve ser anterior ou igual à data final."
            )
            return

        totais = Service.atendimento_totalizar_por_profissional(
            data_inicio, data_fim
        )
        if not totais:
            st.info("Nenhum profissional cadastrado.")
            return

        dados = [
            {
                "Profissional": profissional.get_nome(),
                "Total de serviços": total,
            }
            for profissional, total in totais
        ]
        tabela = pd.DataFrame(dados)
        st.dataframe(tabela, hide_index=True)
        st.bar_chart(
            tabela.set_index("Profissional"),
            y="Total de serviços",
        )
