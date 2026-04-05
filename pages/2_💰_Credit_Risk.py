import streamlit as st
import pandas as pd
import joblib
import numpy as np
import os
from PIL import Image

# Configuración de la página (debe ser lo primero)
st.set_page_config(
    page_title="Credit Risk Predictor",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Aplicar estilos CSS personalizados
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #1E3A8A;
        text-align: center;
        margin-bottom: 0;
    }
    .sub-header {
        font-size: 1.2rem;
        color: #4B5563;
        text-align: center;
        margin-top: 0;
        margin-bottom: 2rem;
    }
    .prediction-card {
        padding: 2rem;
        border-radius: 1rem;
        text-align: center;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
        margin-top: 2rem;
    }
    .good-risk {
        background-color: #D1FAE5;
        border-left: 8px solid #10B981;
    }
    .bad-risk {
        background-color: #FEE2E2;
        border-left: 8px solid #EF4444;
    }
    .probability-bar {
        height: 20px;
        border-radius: 10px;
        background: linear-gradient(90deg, #EF4444 0%, #F59E0B 50%, #10B981 100%);
        margin: 10px 0;
    }
    .info-box {
        background-color: #EFF6FF;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 4px solid #3B82F6;
        margin-bottom: 1rem;
    }
    .stButton > button {
        background-color: #1E3A8A;
        color: white;
        font-weight: bold;
        border-radius: 0.5rem;
        padding: 0.5rem 2rem;
        border: none;
        transition: all 0.3s;
    }
    .stButton > button:hover {
        background-color: #2563EB;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.2);
    }
    .footer {
        text-align: center;
        color: #9CA3AF;
        margin-top: 3rem;
        font-size: 0.9rem;
    }
</style>
""", unsafe_allow_html=True)

# --- LOGO PERSONAL ---
IMAGE_FILENAME = "logo c.png"

if os.path.exists(IMAGE_FILENAME):
    col1, col2, col3 = st.columns([1, 1.5, 1])
    with col2:
        image = Image.open(IMAGE_FILENAME)
        st.image(image, use_container_width=True)
else:
    st.error(f"⚠️ No se encontró el archivo de imagen '{IMAGE_FILENAME}' en la carpeta actual.")

# Título principal con emoji
st.markdown('<p class="main-header">💰 Credit Risk Predictor</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Enter applicant information to predict credit risk (Good / Bad)</p>', unsafe_allow_html=True)

# Cargar modelo y encoders con caché para mejorar rendimiento
@st.cache_resource
def load_model():
    return joblib.load("extra_trees_credit_model.pkl")

@st.cache_resource
def load_encoders():
    encoders = {}
    for col in ["Sex", "Housing", "Saving accounts", "Checking account"]:
        try:
            encoders[col] = joblib.load(f"{col}_encoder.pkl")
        except FileNotFoundError:
            st.error(f"Encoder for {col} not found. Please check the file.")
            st.stop()
    return encoders

try:
    model = load_model()
    encoders = load_encoders()
except Exception as e:
    st.error(f"Error loading model or encoders: {e}")
    st.stop()

# Crear columnas para organizar los inputs
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### 👤 Personal Info")
    age = st.number_input("Age", min_value=18, max_value=100, value=30, step=1, help="Applicant's age in years")
    sex = st.selectbox("Sex", options=["male", "female"], help="Gender of the applicant")
    job = st.selectbox("Job Level", options=[0, 1, 2, 3], index=1, help="0 = unskilled, 1 = unskilled resident, 2 = skilled, 3 = highly skilled")

with col2:
    st.markdown("### 🏠 Housing & Accounts")
    housing = st.selectbox("Housing", options=["own", "rent", "free"], help="Type of housing")
    saving_accounts = st.selectbox("Saving Accounts", options=["little", "moderate", "rich", "quite rich"], help="Status of saving account")
    checking_account = st.selectbox("Checking Account", options=["little", "moderate", "rich"], help="Status of checking account")

with col3:
    st.markdown("### 💳 Loan Details")
    credit_amount = st.number_input("Credit Amount", min_value=0, value=1000, step=100, help="Amount requested")
    duration = st.number_input("Duration (months)", min_value=1, value=12, step=1, help="Loan duration in months")

# Botón de predicción centrado
st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
predict_button = st.button("🔮 Predict Risk")
st.markdown("</div>", unsafe_allow_html=True)

if predict_button:
    # Crear DataFrame de entrada con transformación de categorías
    try:
        input_data = {
            "Age": [age],
            "Sex": [encoders["Sex"].transform([sex])[0]],
            "Job": [job],
            "Housing": [encoders["Housing"].transform([housing])[0]],
            "Saving accounts": [encoders["Saving accounts"].transform([saving_accounts])[0]],
            "Checking account": [encoders["Checking account"].transform([checking_account])[0]],
            "Credit amount": [credit_amount],
            "Duration": [duration]
        }
        input_df = pd.DataFrame(input_data)
        
        # Realizar predicción
        prediction = model.predict(input_df)[0]
        proba = model.predict_proba(input_df)[0]  # [prob_bad, prob_good]
        
        # Mostrar resultado en una tarjeta
        if prediction == 1:
            st.markdown(f"""
            <div class="prediction-card good-risk">
                <h2 style="color: #065F46;">✅ GOOD RISK</h2>
                <p style="font-size: 1.2rem;">Probability of Good: <strong>{proba[1]*100:.1f}%</strong></p>
                <p>Probability of Bad: {proba[0]*100:.1f}%</p>
                <div class="probability-bar" style="width: {proba[1]*100}%; background: #10B981; height: 20px; border-radius: 10px;"></div>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div class="prediction-card bad-risk">
                <h2 style="color: #991B1B;">❌ BAD RISK</h2>
                <p style="font-size: 1.2rem;">Probability of Bad: <strong>{proba[0]*100:.1f}%</strong></p>
                <p>Probability of Good: {proba[1]*100:.1f}%</p>
                <div class="probability-bar" style="width: {proba[0]*100}%; background: #EF4444; height: 20px; border-radius: 10px;"></div>
            </div>
            """, unsafe_allow_html=True)
        
        # Información adicional: factores importantes (opcional)
        st.markdown("---")
        with st.expander("📊 View input data and feature importance (for this prediction)"):
            st.write("Input values (encoded):")
            st.dataframe(input_df)
            # Podríamos mostrar la importancia global del modelo
            st.write("Global Feature Importance (from model):")
            if hasattr(model, "feature_importances_"):
                feature_names = ["Age", "Sex", "Job", "Housing", "Saving accounts", "Checking account", "Credit amount", "Duration"]
                importance_df = pd.DataFrame({
                    "Feature": feature_names,
                    "Importance": model.feature_importances_
                }).sort_values("Importance", ascending=False)
                st.bar_chart(importance_df.set_index("Feature"))
    except Exception as e:
        st.error(f"An error occurred during prediction: {e}")

# Pie de página
st.markdown('<p class="footer">Powered by Machine Learning | Extra Trees Classifier</p>', unsafe_allow_html=True)