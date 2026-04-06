# 🚀 AI Financial Solutions Hub

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.31.0-FF4B4B.svg)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-1.4.0-F7931E.svg)
![Pandas](https://img.shields.io/badge/Pandas-2.2.0-150458.svg)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Predictive%20Modeling-success)

**Author:** Thayss-tech  
**Live Application:** [🔗 Access the Financial Hub here](LINK_DE_TU_APP_EN_STREAMLIT) *(Note: Replace with your actual Streamlit link)*

---

## 📌 Project Overview

The **AI Financial Solutions Hub** is a centralized, multi-page web application designed to deploy and showcase enterprise-level Machine Learning models for the financial sector. Built with Streamlit, this hub serves as an interactive portfolio demonstrating end-to-end data science capabilities, from complex data preprocessing and model training to cloud deployment.

The hub currently features two specialized predictive models:

### 1. 🛡️ Fraud Guard (Real-Time Transaction Screening)
A robust classification pipeline engineered to detect fraudulent activities in mobile money transactions. 
* **Challenge:** Dealing with extreme class imbalance (only 0.3% of transactions were actual fraud).
* **Solution:** Implemented advanced algorithmic weighting, data scaling, and a comprehensive Scikit-Learn `Pipeline` to ensure high recall without sacrificing precision.
* **Key Features:** Real-time prediction interface, automated feature scaling, and probability confidence scoring.

### 2. 💰 Credit Risk Predictor (Applicant Default Evaluation)
A predictive decision-support tool that evaluates retail banking applicants to forecast credit default risk.
* **Algorithm:** Powered by an `ExtraTreesClassifier`.
* **Engineering:** Features customized categorical encoding for variables such as Sex, Housing, and Account Status, mapped precisely from historical financial datasets.
* **Key Features:** Dynamic UI, categorized risk assessment (Good/Bad Risk), and automated input transformation.

---

## 🏗️ Architecture & Tech Stack

This project adopts a modular, multi-page architecture, allowing seamless navigation between different machine learning solutions while sharing a unified server environment.
* **Frontend & Web Framework:** Streamlit
* **Data Manipulation:** Pandas, NumPy
* **Machine Learning:** Scikit-Learn (Pipelines, ExtraTrees, Preprocessing)
* **Model Serialization:** Joblib
* **Deployment:** Streamlit Community Cloud

---

## 📁 Repository Structure

```text
ML-Deployment-Hub/
 ┣ 📄 app.py                           # Main landing page and UI configuration
 ┣ 📂 pages/                           # Streamlit multi-page directory
 ┃ ┣ 📄 1_🛡️_Fraud_Guard.py           # Fraud detection app logic
 ┃ ┗ 📄 2_💰_Credit_Risk.py            # Credit risk evaluation app logic
 ┣ 📦 fraud_detection_pipeline.pkl     # Serialized Fraud Pipeline (Model + Scaler)
 ┣ 📦 extra_trees_credit_model.pkl     # Serialized Credit Risk Model
 ┣ 📦 *_encoder.pkl                    # Various categorical encoders for Credit Risk
 ┣ 🖼️ logo c.png                       # UI Branding assets
 ┣ 📋 requirements.txt                 # Environment dependencies
 ┗ 📄 README.md                        # Project documentation
```

---

## 💻 How to Run Locally

If you want to clone this repository and run the Financial Hub on your local machine:

1. **Clone the repository:**
```bash
git clone [https://github.com/TU_USUARIO/ML-Deployment-Web-App.git](https://github.com/TU_USUARIO/ML-Deployment-Web-App.git)
cd ML-Deployment-Web-App
```

2. **Create a virtual environment (Recommended):**
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

3. **Install the required dependencies:**
```bash
pip install -r requirements.txt
```

4. **Launch the Streamlit App:**
```bash
streamlit run app.py
```

*The application will automatically open in your default web browser at http://localhost:8501.*

---

## 🤝 Let's Connect

Looking for a Data Scientist or Machine Learning Engineer who understands both the algorithms and the deployment infrastructure? Feel free to reach out to discuss data strategies, cloud architecture, or potential opportunities.
