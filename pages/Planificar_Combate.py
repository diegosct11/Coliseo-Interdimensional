import streamlit as st
import pandas as pd
import re
from time import sleep

from core import guardar_combates, cargar_combates, cargar_recursos

def recursos_disponibles():                   # ~ Asigna los recursos disponibles ~ #
    if st.session_state.ocupados["armas"] != []:
        if st.session_state.pelea["Categoría"] == "Con Poderes":
            st.session_state.libres["combatientes"]["con_poderes"] = [combatiente for combatiente in st.session_state.libres["combatientes"]["con_poderes"] if combatiente not in st.session_state.ocupados["combatientes"]["con_poderes"]]
        if st.session_state.pelea["Categoría"] == "Sin Poderes":
            st.session_state.libres["combatientes"]["sin_poderes"] = [combatiente for combatiente in st.session_state.libres["combatientes"]["sin_poderes"] if combatiente not in st.session_state.ocupados["combatientes"]["sin_poderes"]]
        st.session_state.libres["armas"] = [arma for arma in st.session_state.libres["armas"] if arma not in st.session_state.ocupados["armas"]]
    
def validar_combatiente(combatiente):            # ~ Robot Valido ~ #

    if combatiente == "A":
        if st.session_state.pelea["Combatiente_A"] != None:
            return False, "Ya escogió al Combatiente A."
        if Combatiente_A == None or Arma_A == None:
            return False, "Debe llenar todos los campos disponibles."
        
    if combatiente == "B":
        if st.session_state.pelea["Combatiente_B"] != None:
            return False, "Ya escogió al Combatiente A."
        if Combatiente_B == None or Arma_B == None:
            return False, "Debe llenar todos los campos disponibles."
    
    return True, ''

def validar_patrocinador():                     # ~ Patrocinador Valido ~ #
    
    for patron in st.session_state.combates_planificados:
        if Patrocinador == patron:
            return False, "Ya existe un Patrocinador con este nombre, escriba otro."
    
    if not re.match(r'^[A-Za-z\\\\s-]+$', Patrocinador):
        return False, "Patrocinador solo debe contener letras y guiones."
    
    if len(Patrocinador) < 2:
        return False, "Patrocinador debe tener al menos 2 caracteres"
    
    return True, ""

def validar_contienda():               # ~ Campos vacios ~ #
    campos_invalidos = []
    for key, value in st.session_state.pelea.items():
        if not value:
            campos_invalidos.append(key)
    
    if len(campos_invalidos) == 0:
        return True, "" 
    else:
        return False, campos_invalidos 
    
def reset():                 # ~ Resetea los datos de la web ~ #
    st.session_state.pelea.update({
        "Patrocinador": None,
        "Fecha": None,
        "Sala": None,
        "Categoría": None,
        "Combatiente_A": None,
        "Arma_A": None,
        "Combatiente_B": None,
        "Arma_B": None
    })
    
    st.session_state.recursos.update(cargar_recursos())
    
    st.session_state.combates_planificados.update(cargar_combates())
    
    st.session_state.libres = {
        "combatientes" : {
            "con_poderes": [],
            "sin_poderes": []
        },
        "armas" : [],
        "salas" : []
    }
    
    st.session_state.ocupados = {
        "combatientes" : {
            "con_poderes": [],
            "sin_poderes": []
        },
        "armas" : []
    }
    
    st.session_state.fecha_anterior = None
    
    st.session_state.categoría_anterior = None

if "pelea" not in st.session_state:
    st.session_state.pelea = {
        "Patrocinador": None,
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
        "combatientes" : {
            "con_poderes": [],
            "sin_poderes": []
        },
        "armas" : None,
        "salas" : None
    }

if "ocupados" not in st.session_state:                # ~ Recursos usados ~ #
    st.session_state.ocupados = {
        "combatientes" : {
            "con_poderes": [],
            "sin_poderes": []
        },
        "armas" : []
    }

if "categoría_anterior" not in st.session_state:               # ~ Control modo ~ #
    st.session_state.categoría_anterior = None

st.header(
    ":yellow[Gestiona tu Propia] :red[Masacre]",
    text_alignment = "center",
    anchor= False
    )

st.subheader(
    body=":yellow[Fecha de la Contienda]", 
    text_alignment="center", 
    anchor=False
    )

Fecha = st.date_input(    
    label="**Seleccione un Día:**", 
    min_value="today", 
    value=st.session_state.pelea["Fecha"],
    format="DD/MM/YYYY",
    help="*Fecha* en la que se efectuará la pelea."
    )

if Fecha != st.session_state.fecha_anterior:
    
    st.session_state.pelea["Combatiente_A"] = None
    st.session_state.pelea["Combatiente_B"] = None
    st.session_state.pelea["Arma_A"] = None
    st.session_state.pelea["Arma_B"] = None
    st.session_state.pelea["Sala"] = None
    st.session_state.ocupados = {
        "combatientes" : {
            "con_poderes": [],
            "sin_poderes": []
        },
        "armas" : []
    }
    salas_ocupadas = []
    combatientes_ocupados = {
            "con_poderes": [],
            "sin_poderes": []
        }
    armas_ocupadas = []
    
    for combate in st.session_state.combates_planificados.values():           # ~ Selecciona recursos de fechas iguales ~ #
        
        if combate["Fecha"] == str(Fecha):
            salas_ocupadas.append(combate["Sala"])
            if combate["Categoría"] == "Con Poderes":
                combatientes_ocupados["con_poderes"].append(combate["Combatiente_A"])
                combatientes_ocupados["con_poderes"].append(combate["Combatiente_B"])
            else:
                combatientes_ocupados["sin_poderes"].append(combate["Combatiente_A"])
                combatientes_ocupados["sin_poderes"].append(combate["Combatiente_B"]) 
            if combate["Arma_A"] != "Ninguna":
                armas_ocupadas.append(combate["Arma_A"])
            if combate["Arma_B"] != "Ninguna": 
                armas_ocupadas.append(combate["Arma_B"])
                
    if len(salas_ocupadas) == 0:                                      # ~ Define los recursos libres ~ #
        st.success("El Coliseo está libre ese día, planifica una :red[Masacre].")   
        st.session_state.pelea["Fecha"] = str(Fecha)
        st.session_state.libres["salas"] = [salas for salas in st.session_state.recursos["salas"]]
        st.session_state.libres["combatientes"]["con_poderes"] = [combatiente for combatiente in st.session_state.recursos["combatientes"].keys() if st.session_state.recursos["combatientes"][combatiente] == "Con Poderes"]
        st.session_state.libres["combatientes"]["sin_poderes"] = [combatiente for combatiente in st.session_state.recursos["combatientes"].keys() if st.session_state.recursos["combatientes"][combatiente] == "Sin Poderes"]
        st.session_state.libres["armas"] = [arma for arma in st.session_state.recursos["armas"]]

    elif len(salas_ocupadas) >= len(st.session_state.recursos["salas"]):
        st.error("Todas las salas están llenas ese día, busca otro para la :red[Destrución].")
        st.session_state.pelea["Fecha"] = None
        st.session_state.libres["salas"] = []
        
    else:
        st.info("Saldrán solo las salas, los combatientes y armas libres en el día escogido.")
        st.session_state.libres["salas"] = [salas for salas in st.session_state.recursos["salas"] if salas not in salas_ocupadas]
        st.session_state.libres["combatientes"]["con_poderes"] = [combatiente for combatiente in st.session_state.recursos["combatientes"].keys() if st.session_state.recursos["combatientes"][combatiente] == "Con Poderes" and combatiente not in combatientes_ocupados["con_poderes"]]
        st.session_state.libres["combatientes"]["sin_poderes"] = [combatiente for combatiente in st.session_state.recursos["combatientes"].keys() if st.session_state.recursos["combatientes"][combatiente] == "Sin Poderes" and combatiente not in combatientes_ocupados["sin_poderes"]]
        st.session_state.libres["armas"] = [arma for arma in st.session_state.recursos["armas"] if arma not in armas_ocupadas]   
        st.session_state.pelea["Fecha"] = str(Fecha)    
    
    st.session_state.fecha_anterior = Fecha

st.subheader(
    ":yellow[Sala de la Contienda]",
    text_alignment = "center",
    anchor=False
)

Sala = st.selectbox(
    label="**Seleccione una Sala:**",
    options=st.session_state.libres["salas"],
    help="Sala donde se desarrollará el combate.",
    index=None, 
    )

if Sala:
    st.session_state.pelea["Sala"] = Sala

st.subheader(
    ":yellow[Categoría de la Contienda]",
    text_alignment = "center",
    anchor=False
)
with st.container(horizontal_alignment="center"):
    st.session_state.pelea["Categoría"] = st.radio(
        label="**Seleccione una Categoría:**",
        options=["Con Poderes", "Sin Poderes"],
        help="Categoría en la cual se desarrollará la pelea.",
        index=0
    )

if st.session_state.pelea["Categoría"] != st.session_state.categoría_anterior:         # ~ Control con cambio de modo ~ #     
    st.session_state.pelea["Combatiente_A"] = None
    st.session_state.pelea["Combatiente_B"] = None
    st.session_state.pelea["Arma_A"] = None
    st.session_state.pelea["Arma_B"] = None
    
    st.session_state.ocupados = {
        "combatientes" : {
            "con_poderes": [],
            "sin_poderes": []
        },
        "armas" : []
    }
    st.session_state.categoría_anterior = st.session_state.pelea["Categoría"]
    st.rerun()
    

st.subheader(
    ":yellow[Combatientes de la Contienda]",
    text_alignment = "center",
    anchor=False
)


# recursos_disponibles()

col1, col2 = st.columns(
    2, 
    gap = "large", 
    vertical_alignment="center"
    )

with col1:                      # ~ Asignacion Equipo A ~ #
    st.subheader(
        body=":green[Combatiente A]", 
        text_alignment="center",
        anchor=False
        )       
    
    with st.form(
        key="Form_Combatiente_A",
        clear_on_submit=True,
        enter_to_submit=True
        ):


        if st.session_state.pelea["Categoría"] == "Con Poderes":       
            Combatiente_A = st.selectbox(
                "**Seleccione el Combatiente A:**",
                options= [combatiente for combatiente in st.session_state.libres["combatientes"]["con_poderes"] if combatiente not in st.session_state.ocupados["combatientes"]["con_poderes"]],
                index=None,
                )
        else:
            Combatiente_A = st.selectbox(
                "**Seleccione el Combatiente A:**",
                options= [combatiente for combatiente in st.session_state.libres["combatientes"]["sin_poderes"] if combatiente not in st.session_state.ocupados["combatientes"]["sin_poderes"]],
                index=None,
                )
        
        if st.session_state.pelea["Categoría"] == "Sin Poderes":
            Arma_A = st.selectbox(
                "**Seleccione un Arma para el Combatiente A:**",
                options=[ arma for arma in st.session_state.libres["armas"] if arma not in st.session_state.ocupados["armas"]],
                index=None,
                )
        else:
            Arma_A = st.selectbox(
                "**Seleccione un Arma para el Combatiente A:**",
                options=["Ninguna"],
                index=0,
                disabled=True
                )

        st.write("\n")
        with st.container(
            horizontal_alignment="center"
        ):        
        
            bt_a = st.form_submit_button(
                label="**:green[Confirmar Combatiente A]**",
                help="Agrega al Combatiente A a la Masacre."
                )
            
    st.dataframe(
        pd.Series([st.session_state.pelea["Combatiente_A"], st.session_state.pelea["Arma_A"]], name = "Combatiente A" ),
        hide_index=True
        )

    if bt_a:
        if st.session_state.pelea["Fecha"] != None:
            valido_A, mensaje_A = validar_combatiente("A")      
            if not valido_A:
                st.warning(mensaje_A)
                sleep(1.5)
                st.rerun()
            else:
                st.session_state.pelea["Combatiente_A"] = Combatiente_A
                st.session_state.pelea["Arma_A"] = Arma_A
                if st.session_state.pelea["Categoría"] == "Con Poderes":
                    st.session_state.ocupados["combatientes"]["con_poderes"] += [Combatiente_A]
                else:
                    st.session_state.ocupados["combatientes"]["sin_poderes"] += [Combatiente_A]
                st.session_state.ocupados["armas"] += [Arma_A]
                st.success("Combatiente A añadido.")
                sleep(1.3)
                st.rerun()
        else:
            st.warning("Escoja una Fecha Válida primero.")
            sleep(1.3)
            st.rerun()


with col2:                      # ~ Asignacion Equipo A ~ #
    st.subheader(
        body=":green[Combatiente B]", 
        text_alignment="center",
        anchor=False
        )       
    
    with st.form(
        key="Form_Combatiente_B",
        clear_on_submit=True,
        enter_to_submit=True
        ):
                
        if st.session_state.pelea["Categoría"] == "Con Poderes":       
            Combatiente_B = st.selectbox(
                "**Seleccione el Combatiente B:**",
                options= [combatiente for combatiente in st.session_state.libres["combatientes"]["con_poderes"] if combatiente not in st.session_state.ocupados["combatientes"]["con_poderes"]],
                index=None,
                )
        else:
            Combatiente_B = st.selectbox(
                "**Seleccione el Combatiente B:**",
                options= [combatiente for combatiente in st.session_state.libres["combatientes"]["sin_poderes"] if combatiente not in st.session_state.ocupados["combatientes"]["sin_poderes"]],
                index=None,
                )
        if st.session_state.pelea["Categoría"] == "Sin Poderes":
            Arma_B = st.selectbox(
                "**Seleccione un Arma para el Combatiente B:**",
                options=[ arma for arma in st.session_state.libres["armas"] if arma not in st.session_state.ocupados["armas"]],
                index=None,
                )
        else:
            Arma_B = st.selectbox(
                "**Seleccione un Arma para el Combatiente A:**",
                options=["Ninguna"],
                index=0,
                disabled=True
                )
        
        st.write("\n")
        with st.container(
            horizontal_alignment="center"
        ):        
        
            bt_b = st.form_submit_button(
                label="**:green[Confirmar Combatiente B]**",
                help="Agrega al Combatiente B a la Masacre."
                )
            
    st.dataframe(
        pd.Series([st.session_state.pelea["Combatiente_B"], st.session_state.pelea["Arma_B"]], name = "Combatiente B" ),
        hide_index=True
        )
    
    if bt_b:
        if st.session_state.pelea["Fecha"] != None:
            valido_B, mensaje_B = validar_combatiente("B")      
            if not valido_B:
                st.warning(mensaje_B)
                sleep(1.5)
                st.rerun()
            else:
                st.session_state.pelea["Combatiente_B"] = Combatiente_B
                st.session_state.pelea["Arma_B"] = Arma_B
                if st.session_state.pelea["Categoría"] == "Con Poderes":
                    st.session_state.ocupados["combatientes"]["con_poderes"] += [Combatiente_B]
                else:
                    st.session_state.ocupados["combatientes"]["sin_poderes"] += [Combatiente_B]
                st.session_state.ocupados["armas"] += [Arma_B]
                st.success("Combatiente B añadido.")
                sleep(1.3)
                st.rerun()
        else:
            st.warning("Escoja una Fecha Válida primero.")
            sleep(1.3)
            st.rerun()

st.subheader(
    body=":yellow[Patrocinador de la Contienda]",
    text_alignment="center",
    anchor=False
    )

if st.session_state.pelea["Fecha"] != None:
    Patrocinador = st.text_input(
        label="**Escriba el nombre del Patrocinador:**",
        value=st.session_state.pelea["Patrocinador"],
        max_chars=20,
        help="*Patrocinador* de la **contienda**.",
        placeholder="Escriba un nombre."
        )
else:
    Patrocinador = st.text_input(
        label="**Escriba el nombre de un Patrocinador para el combate:**",
        help="*Encargado* o *Responsable* del **combate**.",
        disabled=True,
        placeholder="Seleccione una fecha primero."
        )

if Patrocinador:                    # ~ Validacion Patrocinador ~ #
        valid, error = validar_patrocinador()
        if not valid:
            st.error(error)
            st.session_state.pelea["Patrocinador"] = None
        else:
            st.session_state.pelea["Patrocinador"] = Patrocinador
            st.success("Patrocinador Válido.")

col1, col2, col3 = st.columns(
    [0.3, 1.4, 0.3], 
    gap="small",
    vertical_alignment="bottom"
)

with col2:                      
    
    with st.container(
        border=False,
        key= "Menu_Botones",
        vertical_alignment="center"
    ):
        
        col1, col2 = st.columns(
            2,
            gap="small",
            vertical_alignment="center",
        )
        
        with col1:                  # ~ Boton para cancelar ~ #
            with st.container(                          
                key="button_cancel",
                horizontal_alignment="center"
                ):    
                
                bt_cancelar = st.button(
                    label = "**:red[Cancelar] :yellow[Contienda]**",
                    )

        with col2:                  # ~ Boton para confirmar ~ #
            with st.container(
                key="button_confirm",
                horizontal_alignment="center"
                ):    
                
                bt_confirmar = st.button(
                    label = "**:green[Confirmar] :yellow[Contienda]**",
                    )
                
        st.write("\n")

st.write("\n")

if bt_confirmar:                                
    
    val, campos = validar_contienda()
    
    if not val:
        for error in campos:
            st.warning(f"Falta por llenar: {error}")
        sleep(2)
        st.rerun()
    
    else:
        st.success("El combate ha sido programado, que gane el mejor!")
        st.session_state.combates_planificados[st.session_state.pelea["Patrocinador"]] = st.session_state.pelea
        guardar_combates(st.session_state.get("combates_planificados"))
        reset()
        sleep(2)
        st.rerun()
          
if bt_cancelar:
    
    st.info("El combate que estaba organizando a sido cancelado. Gracias por su atención!")
    reset()
    sleep(2)
    st.rerun()