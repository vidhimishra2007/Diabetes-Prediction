#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  2 02:43:26 2025

@author: vidhimishra
"""

import numpy as np
import pickle
import streamlit as st
import os

# ---------------------------------------------------------
# Page configuration (must be the first Streamlit command)
# ---------------------------------------------------------
st.set_page_config(
    page_title="Diabetes Prediction System",
    page_icon="🩺",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# ---------------------------------------------------------
# Load model
# ---------------------------------------------------------
model_path = os.path.join(os.path.dirname(__file__), "DP_model.pkl")

with open(model_path, "rb") as file:
    loaded_model = pickle.load(file)

# ---------------------------------------------------------
# Custom CSS
# ---------------------------------------------------------
st.markdown(
    """
    <style>
    /* Overall app background */
    .stApp {
        background: linear-gradient(160deg, #0f172a 0%, #1e293b 55%, #0f172a 100%);
    }

    /* Hide default streamlit chrome */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}

    /* Header card */
    .header-card {
        background: linear-gradient(135deg, #14b8a6 0%, #0891b2 100%);
        padding: 28px 32px;
        border-radius: 18px;
        margin-bottom: 28px;
        box-shadow: 0 10px 30px rgba(20, 184, 166, 0.25);
        text-align: center;
    }
    .header-card h1 {
        color: white;
        font-size: 2.1rem;
        margin: 0;
        font-weight: 800;
        letter-spacing: -0.5px;
    }
    .header-card p {
        color: rgba(255,255,255,0.9);
        margin-top: 6px;
        font-size: 0.95rem;
    }

    /* Section labels */
    .section-label {
        color: #5eead4;
        font-weight: 700;
        font-size: 0.85rem;
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-bottom: 4px;
        margin-top: 18px;
    }

    /* Input styling */
    div[data-baseweb="input"] > div {
        background-color: #1e293b;
        border: 1px solid #334155;
        border-radius: 10px;
    }
    div[data-baseweb="input"] input {
        color: #e2e8f0;
    }
    label {
        color: #cbd5e1 !important;
        font-weight: 600 !important;
    }

    /* Predict button */
    div.stButton > button {
        background: linear-gradient(135deg, #14b8a6, #0891b2);
        color: white;
        border: none;
        border-radius: 12px;
        padding: 14px 0;
        font-weight: 700;
        font-size: 1.05rem;
        width: 100%;
        margin-top: 24px;
        box-shadow: 0 6px 18px rgba(20, 184, 166, 0.35);
        transition: transform 0.15s ease;
    }
    div.stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 24px rgba(20, 184, 166, 0.45);
    }

    /* Result cards */
    .result-card {
        padding: 22px 26px;
        border-radius: 14px;
        margin-top: 22px;
        font-size: 1.15rem;
        font-weight: 700;
        text-align: center;
    }
    .result-safe {
        background: rgba(34, 197, 94, 0.12);
        border: 1px solid rgba(34, 197, 94, 0.5);
        color: #4ade80;
    }
    .result-risk {
        background: rgba(239, 68, 68, 0.12);
        border: 1px solid rgba(239, 68, 68, 0.5);
        color: #f87171;
    }

    .disclaimer {
        color: #64748b;
        font-size: 0.8rem;
        text-align: center;
        margin-top: 30px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------------------------------------------------------
# Prediction function
# ---------------------------------------------------------
def diabetes_prediction(sample_data):
    sample_data = np.asarray(sample_data, dtype=float).reshape(1, -1)
    prediction = loaded_model.predict(sample_data)

    if prediction[0] == 0:
        return "safe", "✅ The person is NOT diabetic."
    else:
        return "risk", "⚠️ The person IS diabetic."


# ---------------------------------------------------------
# Main app
# ---------------------------------------------------------
def main():

    # Header
    st.markdown(
        """
        <div class="header-card">
            <h1>🩺 Diabetes Prediction System</h1>
            <p>Enter the clinical parameters below to check the diabetes risk</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Layout inputs in two columns for a cleaner look
    col1, col2 = st.columns(2)

    with col1:
        st.markdown('<div class="section-label">Pregnancies</div>', unsafe_allow_html=True)
        Pregnancies = st.number_input("", min_value=0, max_value=20, step=1, key="preg", label_visibility="collapsed")

        st.markdown('<div class="section-label">Blood Pressure</div>', unsafe_allow_html=True)
        BloodPressure = st.number_input("", min_value=0.0, max_value=200.0, step=1.0, key="bp", label_visibility="collapsed")

        st.markdown('<div class="section-label">Insulin Level</div>', unsafe_allow_html=True)
        Insulin = st.number_input("", min_value=0.0, max_value=900.0, step=1.0, key="insulin", label_visibility="collapsed")

        st.markdown('<div class="section-label">Diabetes Pedigree Function</div>', unsafe_allow_html=True)
        DiabetesPedigreeFunction = st.number_input("", min_value=0.0, max_value=3.0, step=0.01, key="dpf", label_visibility="collapsed")

    with col2:
        st.markdown('<div class="section-label">Glucose Level</div>', unsafe_allow_html=True)
        Glucose = st.number_input("", min_value=0.0, max_value=300.0, step=1.0, key="glucose", label_visibility="collapsed")

        st.markdown('<div class="section-label">Skin Thickness</div>', unsafe_allow_html=True)
        SkinThickness = st.number_input("", min_value=0.0, max_value=100.0, step=1.0, key="skin", label_visibility="collapsed")

        st.markdown('<div class="section-label">BMI</div>', unsafe_allow_html=True)
        BMI = st.number_input("", min_value=0.0, max_value=70.0, step=0.1, key="bmi", label_visibility="collapsed")

        st.markdown('<div class="section-label">Age</div>', unsafe_allow_html=True)
        Age = st.number_input("", min_value=1, max_value=120, step=1, key="age", label_visibility="collapsed")

    # Predict button
    if st.button("🔍 Run Diabetes Test"):
        status, message = diabetes_prediction(
            [
                Pregnancies,
                Glucose,
                BloodPressure,
                SkinThickness,
                Insulin,
                BMI,
                DiabetesPedigreeFunction,
                Age,
            ]
        )

        css_class = "result-safe" if status == "safe" else "result-risk"
        st.markdown(
            f'<div class="result-card {css_class}">{message}</div>',
            unsafe_allow_html=True,
        )

    st.markdown(
        '<div class="disclaimer">This tool provides a statistical estimate and is not a substitute for professional medical advice.</div>',
        unsafe_allow_html=True,
    )


if __name__ == "__main__":
    main()
