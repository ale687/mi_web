import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/Photo.png")
    
with col2:
    st.title("Alejandro Ledesma")
    content = """
    ¡Hola! Mi nombre es Alejandro y soy estudiante de Ingeniería en Sistemas de Información. 
    Me apasiona la tecnología, la programación y el desarrollo web. 
    En esta página vas a encontrar más sobre mí, mis proyectos y cómo contactarme.
    """
    st.info(content)