import streamlit as st
from retangulo import Retangulo

class RetanguloUI:
    def main():
        st.header("Calculo com retangulo")
        b = st.text_input("informe a base")
        h = st.text_input("informe a altura")
        if st.button("calcular"):
            r = Retangulo(float(b), float(h))
            st.write(f"área = {r.calc_area():.2f}")
            st.write(f"diagonal = {r.calc_diagonal():.2f}")
            st.write(r)
