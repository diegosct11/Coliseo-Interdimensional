import streamlit as st

st.subheader(":yellow[¿Qué demonios es el Coliseo?]")

st.markdown(
"""
El Coliseo Interdimensional es el sueño de todo villano, una lugar en donde 
Mojo, el extraterrestre interdimensional más temerario de todos los sistemas 
de tiempo intergalácticos, hace posible la planificación de Combates entre todo 
tipo de personajes del Bien, creando Masacres para que sean disfrutadas por todos 
los seguidores de esta jugosa afición.
""",
text_alignment="justify"
)
with st.container(horizontal_alignment="center"):
    st.image("images/coliseo.jpg", caption="**Coliseo Interdimensional**")

col1,col2 = st.columns(2, gap = "medium")
with col1:
    st.subheader(":yellow[¿Interdimensio... Qué?]", text_alignment = "center", anchor=False)
    st.markdown(
    """
    El gran villano Mojo es el regente de este magestuoso evento, 
    aburrido de limitarse a su propia dimensión para organizar sus
    combates logró hacerse con una tecnología capaz de abrir agujeros 
    interdimensionales. Ahora, héroes de distintas dimensiones son 
    traídos aquí para luchar y así entretener a su bullicioso público. 
    """,
    text_alignment="justify"
    )
with col2:
    st.subheader(":yellow[¿Quién vé esa injusticia?]", text_alignment = "center", anchor=False)
    st.markdown(
    """
    Los combates son transmitidos en la gran red de streaming interdimensional 
    creada por el mismo Mojo, también llamada GRSI, donde los patrocinadores 
    del evento disfrutan de sus más locas fantasías viendo como los valientes 
    héroes de sus dimensiones favoritas son puestos en la obligación de pelear 
    entre sí por su supervivencia.
    """,
    text_alignment="justify"
    )
col1,col2 = st.columns(2, gap = "medium")
with col1:
    st.subheader(":yellow[¿Cómo al Mojo ese puede gustarle esto?]")
    st.markdown(
    """
    Mojo pertenece a una raza extraterrestre llamada Spineless y se alimenta 
    de la adoración de sus seguidores haciendo que su vida se extienda y que 
    su poder aumente. Era el dueño de un famoso canal de transmisión intergaláctica 
    llamado "El Mojoverso", que ahora gracias a su nueva tecnología es interdimensional. 
    Es sumamente perverso y disfruta de ver el sufrimiento ajeno.
    """,
    text_alignment="justify"
    )
with col2:
    st.write("\n")
    with st.container(horizontal_alignment="center"):
        st.image("images/mojo.jpg", width=200, caption="**Mojo - el Interdimensional**")

st.divider()

with st.container(horizontal_alignment="center"):
    st.page_link(page="pages/Planificar_Combate.py",label=":red[**Planifica una Masacre aquí**]")