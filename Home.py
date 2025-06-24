import streamlit as st
import pandas as pd

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
    
#col3, empy_col, col4 = st.columns([1.5, 0.5, 1.5])
col3, col4 = st.columns([1, 1])

df = pd.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:5].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row["url"]})")


#with col4:
    #for index, row in df[10:].iterrows():
        #st.header(row["title"])
        #st.write(row["description"])
        #st.image("images/" + row["image"])
        #st.write(f"[Source Code]({row['url']})")