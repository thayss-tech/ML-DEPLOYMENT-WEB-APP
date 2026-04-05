import streamlit as st
import os
from PIL import Image

st.set_page_config(page_title="Thayss ML Hub", page_icon="🧠", layout="centered", initial_sidebar_state="expanded")

st.markdown("""
    <style>
    .main-title { color: #002A8F; text-align: center; font-size: 3rem; font-weight: bold; }
    .sub-title { text-align: center; color: #555; font-size: 1.2rem; margin-bottom: 2rem; }
    .card { padding: 1.5rem; border-radius: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); margin-bottom: 1rem; border-left: 5px solid #EC7000; background-color: #f9f9f9; }
    </style>
""", unsafe_allow_html=True)

IMAGE_FILENAME = "logo c.png"
if os.path.exists(IMAGE_FILENAME):
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        image = Image.open(IMAGE_FILENAME)
        st.image(image, use_container_width=True)

st.markdown('<p class="main-title">Machine Learning Deployment Hub</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">Predictive Intelligence Portfolio by Thayss-tech</p>', unsafe_allow_html=True)
st.divider()

st.markdown("### 👈 Select an application from the sidebar to get started.")
st.write("")

st.markdown("""
<div class="card">
    <h3>🛡️ Fraud Guard (Real-Time Screening)</h3>
    <p>A supervised machine learning pipeline engineered to detect fraudulent transactions. Handles extreme class imbalances using advanced algorithmic weighting.</p>
</div>
<div class="card">
    <h3>💰 Credit Risk Predictor</h3>
    <p>An Extra Trees Classifier deployment that evaluates applicant profiles to predict credit default risk. Features customized categorical encoding and probability scoring.</p>
</div>
""", unsafe_allow_html=True)