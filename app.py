import streamlit as st
import requests
from streamlit_lottie import st_lottie
import pandas as pd
import plotly.express as px

# Función para cargar animaciones Lottie desde una URL
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Configuración del título y descripción de la aplicación
st.title("Proyecto de Estadísticas de Jugadores")
st.write("Este es un análisis interactivo de las estadísticas de los jugadores, mostrando sus valores de mercado.")

# Carga y muestra una animación Lottie
lottie_url = "https://lottie.host/embed/3d48d4b9-51ad-4b7d-9d28-5e248cace11/Rz3QtSCq3.json"
lottie_coding = load_lottieurl(lottie_url)
if lottie_coding:
    st_lottie(lottie_coding, height=200, width=300)

# Crear algunos datos de ejemplo para la tabla
data = {
    'Jugador': ['Jugador A', 'Jugador B', 'Jugador C'],
    'Valor de Mercado': [10, 15, 8]
}
df = pd.DataFrame(data)

# Muestra una tabla en Streamlit
st.subheader("Tabla de Valores de Mercado")
st.table(df)

# Crear y mostrar un gráfico interactivo con Plotly
st.subheader("Gráfico de Valor de Mercado")
fig = px.bar(df, x='Jugador', y='Valor de Mercado', title="Valor de Mercado por Jugador")
st.plotly_chart(fig)
