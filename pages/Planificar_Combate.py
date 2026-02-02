import streamlit as st
from core import guardar_combates, cargar_combates, cargar_recursos

def validar_combatiente_arma(combatiente):
    pass

if "pelea" not in st.session_state:
    st.session_state.pelea = {
        "Nombre": None,
        "Fecha": None,
        "Sala": None,
        "Categoría": None,
        "Combatiente_A": None,
        "Arma_A": None,
        "Combatiente_B": None,
        "Arma_B": None
    }

if "recursos" not in st.session_state:
    st.session_state.recursos = cargar_recursos()

if "combates_planificados" not in st.session_state:
    st.session_state.combates_planificados = cargar_combates()

if "fecha_anterior" not in st.session_state:
    st.session_state.fecha_anterior = None

if "libres" not in st.session_state:             
    st.session_state.libres = {
        "combatientes" : None,
        "armas" : None,
        "salas" : None
    }

st.subheader(
    body="Fechar y lugar:", 
    text_alignment="center", 
    anchor=False
    )

Fecha = st.date_input(    
    label="**Elija una Fecha para el combate:**", 
    min_value="today", 
    value=st.session_state.pelea["Fecha"],
    format="DD/MM/YYYY",
    help="*Fecha* en la cual se desarrollará el combate."
    )

if Fecha != st.session_state.fecha_anterior:

    st.session_state.pelea["Sala"] = None
    
    salas_ocupadas = []
    combatientes_ocupados = []
    armas_ocupadas = []
    
    for combate in st.session_state.combates_planificados.values():           # ~ Selecciona recursos de fechas iguales ~ #
        if combate["Fecha"] == str(Fecha):
            salas_ocupadas.append(combate["Sala"])
            combatientes_ocupados.append(combate["Combatiente_A"])
            combatientes_ocupados.append(combate["Combatiente_B"])
            if combate["Arma_A"] != "Ninguna":
                armas_ocupadas.append(combate["Arma_A"])
            if combate["Arma_B"] != "Ninguna": 
                armas_ocupadas.append(combate["Arma_B"])
                
    if len(salas_ocupadas) == 0:                                      # ~ Define los recursos libres ~ #
        st.success("El Coliseo está libre ese día, planifica una :red[Masacre].")   
        st.session_state.pelea["Fecha"] = str(Fecha)
        st.session_state.libres["salas"] = [salas for salas in st.session_state.recursos["salas"]]
        st.session_state.libres["combatientes"] = [combatiente for combatiente in st.session_state.recursos["combatientes"].keys()]
        st.session_state.libres["armas"] = [arma for arma in st.session_state.recursos["armas"]]

    elif len(salas_ocupadas) >= len(st.session_state.recursos["salas"]):
        st.error("Todas las salas están llenas ese día, busca otro para la :red[Destrución].")
        st.session_state.pelea["Fecha"] = None
        st.session_state.libres["salas"] = []
        
    else:
        st.info("Saldrán solo las salas, los combatientes y armas libres en el día escogido.")
        st.session_state.libres["salas"] = [salas for salas in st.session_state.recursos["salas"] if salas not in salas_ocupadas]
        st.session_state.libres["combatientes"] = [combatiente for combatiente in st.session_state.recursos["combatientes"].keys() if combatiente not in combatientes_ocupados]
        st.session_state.libres["armas"] = [arma for arma in st.session_state.recursos["armas"] if arma not in armas_ocupadas]   
        st.session_state.pelea["Fecha"] = str(Fecha)    
    
    st.session_state.fecha_anterior = str(Fecha)