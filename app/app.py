import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("model/house_price_model.pkl")

# ---------- PAGE SETTINGS ----------
st.set_page_config(
    page_title="House Price Prediction",
    page_icon="🏠",
    layout="centered"
)

# ---------- CUSTOM DESIGN ----------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #061a40 0%, #0b3d91 50%, #001f54 100%);
}

.block-container {
    max-width: 850px;
    padding-top: 3rem;
}

.title {
    text-align: center;
    color: white;
    font-size: 42px;
    font-weight: 800;
    margin-bottom: 5px;
}

.subtitle {
    text-align: center;
    color: #eef8ff;
    font-size: 18px;
    margin-bottom: 30px;
}

.card {
    background: rgba(255,255,255,0.94);
    padding: 35px;
    border-radius: 25px;
    box-shadow: 0 10px 35px rgba(0,0,0,0.18);
}

.result {
    background: #dff8ef;
    border: 2px solid #9ee7d0;
    padding: 18px;
    border-radius: 15px;
    color: #087f5b;
    text-align: center;
    font-size: 24px;
    font-weight: 700;
    margin-top: 25px;
}

.stButton > button {
    width: 100%;
    background: linear-gradient(90deg, #1677e8, #2563eb);
    color: white;
    border: none;
    border-radius: 12px;
    padding: 14px;
    font-size: 18px;
    font-weight: 700;
}

.stButton > button:hover {
    background: linear-gradient(90deg, #125fc0, #1d4ed8);
}
</style>
""", unsafe_allow_html=True)

# ---------- HEADER ----------
st.markdown(
    '<div class="title">🏠 House Price Prediction</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Enter the details below to predict the estimated price of a house.</div>',
    unsafe_allow_html=True
)

# ---------- INPUT CARD ----------
st.markdown('<div class="card">', unsafe_allow_html=True)

bedrooms = st.number_input(
    "🛏️ Number of Bedrooms",
    min_value=0,
    value=3
)

bathrooms = st.number_input(
    "🛁 Number of Bathrooms",
    min_value=0.0,
    value=2.0
)

living_area = st.number_input(
    "🏠 Living Area (sq ft)",
    min_value=0.0,
    value=2000.0
)

lot_area = st.number_input(
    "📐 Lot Area (sq ft)",
    min_value=0.0,
    value=5000.0
)

floors = st.number_input(
    "🏢 Number of Floors",
    min_value=0.0,
    value=1.0
)

st.markdown("</div>", unsafe_allow_html=True)

# ---------- PREDICTION ----------
if st.button(" Predict House Price"):

    st.write("Button clicked!")

    try:
        house = pd.DataFrame({
            "number of bedrooms": [bedrooms],
            "number of bathrooms": [bathrooms],
            "living area": [living_area],
            "lot area": [lot_area],
            "number of floors": [floors]
        })

        predicted_price = model.predict(house)[0]

        st.success(f"🏠 Estimated House Price: ${predicted_price:,.2f}")

    except Exception as e:
        st.error(f"Prediction Error: {e}")