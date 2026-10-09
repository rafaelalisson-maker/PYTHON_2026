import streamlit as st
import time
from service import Service


class ConfirmarServicoUI:

    @staticmethod
    def main():
        st.header("Confirmar Serviço")

        # Busca os serviços aguardando confirmação para o profissional logado
        horarios = Service.horario_confirmar_servico(st.session_state["usuario_id"])

        if len(horarios) == 0:
            st.write("Nenhum serviço pendente de confirmação.")
        else:
            clientes = Service.cliente_listar()

            op = st.selectbox("Informe o horário", horarios)

            # Localiza o cliente associado ao horário
            id_cliente = None if op.get_id_cliente() in [0, None] else op.get_id_cliente()
            index_cliente = next(
                (i for i, c in enumerate(clientes) if c.get_id() == id_cliente),
                0
            ) if clientes else None

            cliente = st.selectbox(
                "Cliente",
                clientes,
                index=index_cliente,
                disabled=True
            )

            if st.button("Confirmar"):
                cli_id = cliente.get_id() if cliente else op.get_id_cliente()

                # Atualiza o horário marcando 'confirmado' como True
                Service.horario_atualizar(
                    op.get_id(),
                    op.get_data(),
                    True,
                    cli_id,
                    op.get_id_servico(),
                    op.get_id_profissional()
                )

                st.success("Horário confirmado com sucesso!")
                time.sleep(1)
                st.rerun()