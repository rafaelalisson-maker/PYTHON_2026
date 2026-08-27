from templates.manterclienteui import manterclienteui
from templates.manterservicoui import manterservicoui
import streamlit as st

class indexUI:
    def main():
        op = sidebar.slectbox("meno, ["clientes, Serviços]")
        if op == "clientes": manterclienteui.main()
        if op == "serviços": manterservicoui.main()

indexUI.main()



