import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/Photo.png", width=300)
    
with col2:
    st.title("Claudio Ledesma")
    content = """
    ¡Hola! Mi nombre es Claudio y soy estudiante de Ingeniería en Sistemas de Información.  
    Me encuentro en formación constante en el área de desarrollo de software, con especial interés 
    en la programación con Python, el desarrollo web y la integración de APIs.  

    Esta página tiene como objetivo presentar mis proyectos, habilidades técnicas y 
    formas de contacto para futuras oportunidades laborales en el ámbito IT.
    """
    st.info(content)
    
st.subheader("Tecnologías que utilizo")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("🐍 **Python**")
    st.markdown("🗄️ **SQL**")
    st.markdown("🗃️ **Git / GitHub**")
    
with col2:
    st.markdown("🧱 **HTML básico**")
    st.markdown("📡 **APIs**")
    st.markdown("🌐 **Streamlit**")

with col3:
    st.markdown("📊 **Análisis de datos básico**")
    st.markdown("🔀 **Automatización de tareas**")
    st.markdown("🛠️ **Trabajo en equipo y resolución de problemas**")
    
col3, col4, col5 = st.columns([0.5, 1, 0.5])

df = pd.read_csv("data.csv", sep=";")

with col4:
    for index, row in df[:5].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row["url"]})")

