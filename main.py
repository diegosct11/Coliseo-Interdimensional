import streamlit as st

st.title(
    body="🌿:yellow[COLISEO INTERDIMENSIONAL]🌿",
    anchor=False,
    text_alignment="center"
)
st.header(
    body=":green[Lucha de Titanes]",
    anchor=False,
    text_alignment="center")

st.divider()

Info_EL_Coliseo = st.Page(
    page="pages/Info_EL_Coliseo.py",
    title="Info - El Coliseo",
    icon=":material/search:",
    default=True
)
Planificar_Combate = st.Page(
    page="pages/Planificar_Combate.py",
    title="Planificar Combate",
    icon=":material/add:"
)
Listado_de_Combates = st.Page(
    page="pages/Listado_de_Combates.py",
    title="Listado de Combates",
    icon=":material/book:"
)
Combatientes = st.Page(
    page="pages/Combatientes.py",
    title="Combatientes",
    icon=":material/swords:"
)
nav = st.navigation({
    "Información:": [Info_EL_Coliseo],
    "Contienda:":[Planificar_Combate, Listado_de_Combates],
    "Sumario:":[Combatientes]
    })
nav.run()
