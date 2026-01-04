import streamlit as st
from pathlib import Path
import base64

st.set_page_config(
    page_title="Prioritas Penanganan Sampah",
    layout="wide",
    initial_sidebar_state="collapsed"
)

def load_css():
    css_file = Path("style.css")
    if css_file.exists():
        with open(css_file) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

hero_image = Path("assets/hero3.png")

if hero_image.exists():
    encoded_image = base64.b64encode(hero_image.read_bytes()).decode()

    st.markdown(
        f"""
        <div class="hero-container">
            <img src="data:image/jpg;base64,{encoded_image}" class="hero-img"/>
            <div class="hero-overlay"></div>
            <div class="hero-text">
               <h1>Prioritas Penanganan Sampah<br>Kota Tasikmalaya</h1>
                <p>
                    Sistem prediksi timbulan sampah berbasis Machine Learning
                    untuk menentukan prioritas penanganan sampah di setiap
                    kecamatan di Kota Tasikmalaya secara objektif dan terukur.
                </p>
                <a href="Prediksi" class="hero-btn">Mulai Prediksi</a>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

# ================= PROBLEM =================
st.markdown("## Permasalahan yang Dihadapi")

col1, col2 = st.columns([1, 1], gap="large")

with col1:
    st.markdown(
        """
        <p class="problem-text">
        Peningkatan jumlah penduduk dan aktivitas masyarakat di Kota Tasikmalaya
        menyebabkan volume timbulan sampah yang terus meningkat setiap tahunnya.
        Permasalahan utama yang dihadapi adalah keterbatasan sumber daya dalam
        penanganan sampah, sehingga diperlukan penentuan prioritas penanganan
        yang tepat pada setiap kecamatan. Tanpa pendekatan berbasis data,
        pengambilan keputusan berpotensi menjadi kurang efektif dan tidak merata.
        Oleh karena itu, diperlukan sistem prediksi timbulan sampah yang mampu
        membantu pemerintah daerah dalam menentukan prioritas penanganan sampah
        secara lebih terukur dan berbasis data historis.
        </p>
        """,
        unsafe_allow_html=True
    )

with col2:
    st.image("assets/problem3.png", use_container_width=True)

# ================= SOLUTION =================
st.markdown(
    "<h2 style='text-align: center; margin-bottom: 2rem;'>Solusi yang Ditawarkan</h2>",
    unsafe_allow_html=True
)

c1, c2, c3 = st.columns(3)

def get_base64_img(path):
    with open(path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

img1 = f"data:image/png;base64,{get_base64_img('assets/solution1.png')}"
img2 = f"data:image/png;base64,{get_base64_img('assets/solution2.png')}"
img3 = f"data:image/png;base64,{get_base64_img('assets/solution3.png')}"

with c1:
    st.markdown(f"""
        <div class="card-container">
            <img src="{img1}" class="card-img"/>
            <div class="card-content">
                <h3>Prediction & Ranking</h3>
                <p>
                Menyediakan hasil prediksi timbulan sampah pada setiap kecamatan
                beserta peringkat prioritas penanganannya berdasarkan metode
                Linear Regression.
                </p>
            </div>
        </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown(f"""
        <div class="card-container">
            <img src="{img2}" class="card-img"/>
            <div class="card-content">
                <h3>Decision Support</h3>
                <p>
                Mendukung pengambilan keputusan dalam penanganan sampah melalui
                analisis data historis dan prediksi berbasis Machine Learning.
                </p>
            </div>
        </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown(f"""
        <div class="card-container">
            <img src="{img3}" class="card-img"/>
            <div class="card-content">
                <h3>User Friendly</h3>
                <p>
                Antarmuka sistem dirancang sederhana dan intuitif sehingga mudah
                digunakan oleh pengguna untuk melihat hasil prediksi dan prioritas.
                </p>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
