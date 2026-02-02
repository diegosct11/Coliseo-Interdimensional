import streamlit as st
import pandas as pd
from time import sleep
from core import cargar_combates, guardar_combates

if "combates_planificados" not in st.session_state:                  # ~ Combates programados ~ #
    st.session_state.combates_planificados = cargar_combates()

st.header(":yellow[Listado de Combates]", text_alignment="center", anchor= False)

dataframe_peleas = pd.DataFrame.from_dict(
    data=st.session_state.combates_planificados,
    orient="index"
)

st.dataframe(
    data=dataframe_peleas,
    width="stretch",
    height="auto",
    hide_index=True,
    column_order=["Patrocinador", "Fecha", "Sala", "Combatiente_A", "Arma_A", "Combatiente_B", "Arma_B"]
)

st.subheader(":yellow[Borrar Contienda]", text_alignment="center", anchor=False)

borrar = st.selectbox("Evite una :red[Masacre] para planificarla después.",
    options=[combate for combate in st.session_state.combates_planificados.keys()],
    index = None,
    placeholder = "Solo retrasarás una Muerte inevitable."
    )
with st.container(horizontal_alignment="center"):
    boton = st.button("Borrar")

if boton:    
    if borrar == None:
        st.warning("Seleccione primero una Contienda.")
        sleep(1.3)
        st.rerun()
    else:
        st.success("Un combatiente ha sido salvado, por ahora...")
        st.session_state.combates_planificados.pop(borrar)
        guardar_combates(st.session_state.combates_planificados)
        sleep(2)
        st.rerun()