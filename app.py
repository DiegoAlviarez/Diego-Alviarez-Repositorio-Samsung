# Importa las bibliotecas necesarias
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

# Cargar el archivo CSV desde GitHub
file_path = 'https://raw.githubusercontent.com/AndersonP444/PROYECTO-SIC-JAKDG/main/valores_mercado_actualizados.csv'
df = pd.read_csv(file_path)

# Muestra la tabla de datos del CSV
st.subheader("Tabla de Valores de Mercado")
st.dataframe(df)

# Crear y mostrar un gráfico interactivo con Plotly basado en los datos del CSV
st.subheader("Gráfico de Valor de Mercado")
fig = px.bar(df, x='Jugador', y='Valor de Mercado', title="Valor de Mercado por Jugador")
st.plotly_chart(fig)

