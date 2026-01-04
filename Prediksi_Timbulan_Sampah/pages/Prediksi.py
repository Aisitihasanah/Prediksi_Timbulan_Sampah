import streamlit as st
import joblib
import pandas as pd
from pathlib import Path

# ================= CONFIG =================
st.set_page_config(
    page_title="Prediksi Prioritas Sampah",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ================= LOAD CSS =================
def load_css():
    if Path("style.css").exists():
        with open("style.css") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

# ================= LOAD MODEL =================
@st.cache_resource
def load_assets():
    model = joblib.load("models/model_lr_sampah.pkl")
    encoder = joblib.load("models/encoder_kecamatan.pkl")
    return model, encoder

model, encoder = load_assets()

# ================= BACK BUTTON =================
if st.button("⬅\nKembali"):
    st.switch_page("app.py")

# ================= HEADER =================
st.markdown(
    '<h1 style="color:#ffb800; font-size:3rem; font-weight:800;">'
    'Prediksi Prioritas Penanganan Sampah</h1>',
    unsafe_allow_html=True
)

st.markdown(
    '<p style="color:white; opacity:80%;">'
    'Sistem ini memprediksi timbulan sampah tiap kecamatan di Kota Tasikmalaya '
    'menggunakan metode Linear Regression untuk menentukan prioritas penanganan.'
    '</p>',
    unsafe_allow_html=True
)

st.markdown('<div class="scanner-container">', unsafe_allow_html=True)

# ================= INPUT =================
st.markdown(
    '<p style="color:white; font-weight:600;">Masukkan Parameter Prediksi:</p>',
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)

with col1:
    tahun = st.number_input(
        "Tahun Prediksi",
        min_value=2020,
        max_value=2035,
        value=2025
    )

with col2:
    kecamatan_fokus = st.selectbox(
        "Pilih Kecamatan",
        encoder.classes_
    )

# ================= PREDIKSI =================
if st.button("📊 Prediksi Sekarang"):

    hasil = []

    for kec, enc in zip(encoder.classes_, range(len(encoder.classes_))):
        X = pd.DataFrame({
            "tahun": [tahun],
            "kecamatan_encoded": [enc]
        })
        pred = model.predict(X)[0]
        hasil.append([kec, pred])

    df = pd.DataFrame(
        hasil,
        columns=["Kecamatan", "Prediksi Timbulan"]
    )

    # ================= RANKING =================
    df = df.sort_values(
        by="Prediksi Timbulan",
        ascending=False
    ).reset_index(drop=True)

    df["Ranking"] = df.index + 1

    # ================= PRIORITAS =================
    q75 = df["Prediksi Timbulan"].quantile(0.75)
    q50 = df["Prediksi Timbulan"].quantile(0.50)

    def prioritas(x):
        if x >= q75:
            return "Tinggi"
        elif x >= q50:
            return "Sedang"
        else:
            return "Rendah"

    df["Prioritas"] = df["Prediksi Timbulan"].apply(prioritas)

    fokus = df[df["Kecamatan"] == kecamatan_fokus].iloc[0]

    # ================= OUTPUT FOKUS =================
    st.markdown("### 📍 Kecamatan Fokus")
    st.success(
        f"""
        Kecamatan : {fokus['Kecamatan']}
        \nPrediksi Timbulan : {fokus['Prediksi Timbulan']:.2f}
        \nPrioritas : {fokus['Prioritas']}
        \nRanking : {fokus['Ranking']} dari {len(df)} kecamatan
        """
    )

    # ================= TABEL =================
    st.markdown("### 📋 Daftar Prioritas Seluruh Kecamatan")

    # Penomoran tabel mulai dari 1
    df.index = df.index + 1

    st.dataframe(df, use_container_width=True)

st.markdown('</div>', unsafe_allow_html=True)
