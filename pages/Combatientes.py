import streamlit as st

st.header(":yellow[Colección de Prisioneros]")

tab1, tab2 = st.tabs([":green[**Con poderes**]", ":red[**Sin poderes**]"])

with tab1:
    st.subheader(":green[Con poderes]", text_alignment = "center", anchor = None)
    st.write("\n")
    col1,col2,col3 = st.columns(3, gap="medium", vertical_alignment="top")
    with col1:
        st.image("images/con poderes/Black Panther.jpg", caption="Black Panther")
        st.image("images/con poderes/Flash.jpg", caption= "Flash")
        st.image("images/con poderes/Homelander.jpg", caption="Homelander")
        st.image("images/con poderes/Invincible.jpg", caption="Invencible")
        st.image("images/con poderes/Wonder Woman.jpg", caption="Wonder Woman")
        st.image("images/con poderes/Superman.jpg", caption="Superman")
    with col2:
        st.image("images/con poderes/Capitan America.jpg", caption= "Capitán América")
        st.image("images/con poderes/Cyborg.jpg", caption= "Cyborg")
        st.image("images/con poderes/Green Lantern.jpg", caption="Green Lantern")
        st.image("images/con poderes/Thor.jpg", caption="Thor")
        st.image("images/con poderes/The Hulk.jpg", caption="The Hulk")
    with col3:
        st.image("images/con poderes/Detective Marciano.jpg", caption= "Detective Marciano")
        st.image("images/con poderes/Deadpool.jpg", caption= "Deadpool")
        st.image("images/con poderes/Spiderman.jpg", caption="Spiderman")
        st.image("images/con poderes/Venom.jpg", caption="Venom")
        st.image("images/con poderes/Wolverine.jpg", caption="Wolverine")

with tab2:
    st.subheader(":red[Sin poderes]", text_alignment = "center", anchor = None)
    st.write("\n")
    col1,col2,col3 = st.columns(3, gap="medium", vertical_alignment="top")
    with col1:
        st.image("images/sin poderes/Batman.jpg", caption="Batman")
        st.image("images/sin poderes/Black Widow.jpg", caption= "Black Widow")
        st.image("images/sin poderes/Bruce Lee.jpg", caption="Bruce Lee")
        st.image("images/sin poderes/Daredevil.jpg", caption="Daredevil")
        st.image("images/sin poderes/John Wick.jpg", caption="John Wick")
    with col2:
        st.image("images/sin poderes/Espartaco.jpg", caption= "Espartaco")
        st.image("images/sin poderes/Green Arrow.jpg", caption= "Green Arrow")
        st.image("images/sin poderes/Hawkeye.jpg", caption="Hawkeye")
        st.image("images/sin poderes/Jackie Chan.jpg", caption="Jackie Chan")
        st.image("images/sin poderes/Toni Stark.jpg", caption="Toni Stark")
    with col3:
        st.image("images/sin poderes/Kill Bill.jpg", caption= "Kill Bill")
        st.image("images/sin poderes/Leonidas.jpg", caption= "Leonidas")
        st.image("images/sin poderes/Napoleon.jpg", caption="Napoleon")
        st.image("images/sin poderes/Punisher.jpg", caption="Punisher")
        st.image("images/sin poderes/El Zorro.jpg", caption="El Zorro")
        st.image("images/sin poderes/Elpidio.jpg", caption="Elpidio")

st.divider()

with st.container(horizontal_alignment="center"):
    st.page_link(page="pages/Planificar_Combate.py",label=":red[**Planifica una Masacre aquí**]")