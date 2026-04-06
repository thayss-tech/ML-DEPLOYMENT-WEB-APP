import streamlit as st
import os
from PIL import Image

# 1. Configuración de página (SIEMPRE PRIMERO)
st.set_page_config(
    page_title="Thayss-tech | Financial Hub",
    page_icon="💼",
    layout="wide", # Usamos wide para que las tarjetas no se vean tan estiradas
    initial_sidebar_state="expanded"
)

# 2. Arreglo Profesional del Menú Lateral (Sidebar)
# Con esto quitamos ese título genérico de "app" y ponemos tu marca
st.sidebar.markdown("""
    <div style="text-align: center; margin-bottom: 20px;">
        <h1 style="color: #EC7000; font-family: sans-serif; font-size: 1.5rem;">Thayss-tech Hub</h1>
        <p style="color: #666; font-size: 0.9rem;">Machine Learning Portfolio</p>
    </div>
    <hr style="border: 1px solid #ddd; margin-bottom: 20px;">
""", unsafe_allow_html=True)


# 3. CSS BLINDADO (Fuerza colores legibles sin importar el Modo Oscuro)
st.markdown("""
    <style>
    /* Estilo para el título principal */
    .main-title {
        color: #002A8F; /* Azul Corporativo */
        text-align: center;
        font-size: 2.8rem !important;
        font-weight: bold;
        font-family: 'Helvetica Neue', sans-serif;
        margin-bottom: 0.5rem;
    }
    
    /* Estilo para el subtítulo */
    .sub-title {
        text-align: center;
        color: #555;
        font-size: 1.2rem;
        margin-bottom: 2.5rem;
        font-family: sans-serif;
    }

    /* 🔥 EL ARREGLO DE LAS TARJETAS - FORZANDO COLOR DE TEXTO OPACO */
    .card-container {
        display: flex;
        gap: 20px;
        justify-content: center;
        flex-wrap: wrap;
        margin-top: 20px;
    }

    .card {
        background-color: #FFFFFF !important; /* Fondo Blanco Puro FORZADO */
        color: #1E1E1E !important; /* Texto Casi Negro FORZADO (súper legible) */
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.1);
        border-left: 8px solid #EC7000; /* Borde Naranja Itaú */
        width: 45%;
        min-width: 300px;
        transition: transform 0.3s ease;
    }
    
    /* Efecto hover profesional al pasar el mouse */
    .card:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 35px rgba(0,0,0,0.15);
    }

    /* Colores específicos para títulos dentro de la tarjeta para que NO hereden del Modo Oscuro */
    .card h3 {
        color: #002A8F !important; /* Azul Título */
        margin-top: 0;
        font-size: 1.6rem;
        margin-bottom: 1rem;
    }
    
    .card p {
        color: #333333 !important; /* Texto cuerpo opaco */
        line-height: 1.6;
        font-size: 1rem;
    }

    /* Arreglo para el mensaje de "Select an application" */
    .instruction-text {
        text-align: center;
        color: #EC7000;
        font-weight: bold;
        font-size: 1.3rem;
        margin-top: 30px;
        font-family: sans-serif;
    }
    
    /* Ocultar el header predeterminado de Streamlit para más limpieza */
    [data-testid="stHeader"] {
        background: rgba(0,0,0,0);
        color: rgba(0,0,0,0);
    }
    </style>
""", unsafe_allow_html=True)

# 4. Contenido de la Portada

# Títulos Principales
st.markdown('<p class="main-title">AI Financial Solutions Hub</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">Advanced Machine Learning Deployment Portfolio by Thayss-tech</p>', unsafe_allow_html=True)

st.divider()

# Logo (Opcional, si lo tienes, se verá pro)
IMAGE_FILENAME = "logo c.png"
if os.path.exists(IMAGE_FILENAME):
    # Centramos el logo usando columnas
    col1, col2, col3 = st.columns([1, 0.5, 1])
    with col2:
        image = Image.open(IMAGE_FILENAME)
        st.image(image, use_container_width=True)

# Mensaje de instrucción
st.markdown('<p class="instruction-text">👈 Select a specialized application from the sidebar menu to begin</p>', unsafe_allow_html=True)

st.write("")
st.write("")

# 5. Renderizado de las Tarjetas (Usando la nueva estructura CSS blindada)
st.markdown("""
<div class="card-container">
    <div class="card">
        <h3>🛡️ Fraud Guard</h3>
        <p><strong>Real-Time Transaction Screening.</strong><br>
        A supervised machine learning pipeline engineered to detect fraudulent mobile money transactions. Handles extreme class imbalances (0.3% fraud rate) using advanced algorithmic weighting.</p>
    </div>
    <div class="card">
        <h3>💰 Credit Risk Predictor</h3>
        <p><strong>Applicant Default Evaluation.</strong><br>
        An Extra Trees Classifier deployment that evaluates applicant profiles to predict credit default risk. Features customized categorical encoding and precise probability scoring for financial decision-making.</p>
    </div>
</div>
""", unsafe_allow_html=True)

# Pie de página limpio
st.write("")
st.divider()
st.caption("© 2024 Thayss-tech | All rights reserved. Models deployed for demonstration purposes.")
