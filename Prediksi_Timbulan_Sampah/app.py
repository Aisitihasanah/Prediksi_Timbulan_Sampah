import streamlit as st
from pathlib import Path
import base64

st.set_page_config(
    page_title="Prediksi Timbulan Sampah",
    layout="wide",
    initial_sidebar_state="collapsed"
)

css_file = Path(__file__).parent / "style.css"
if css_file.exists():
    st.markdown(
        f"<style>{css_file.read_text()}</style>",
        unsafe_allow_html=True
    )
else:
    st.warning("style.css tidak ditemukan")

BASE_DIR = Path(__file__).resolve().parent
hero_image_path = BASE_DIR / "assets" / "hero.png"

if hero_image_path.exists():
    encoded_image = base64.b64encode(hero_image_path.read_bytes()).decode()

    st.markdown(
        f"""
        <div class="hero-container">
            <img src="data:image/jpg;base64,{encoded_image}" class="hero-img"/>
            <div class="hero-overlay"></div>
            <div class="hero-text">
                 <h1>Prediksi<br>Timbulan Sampah Kecamatan<br>Kota Tasikmalaya</h1>
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
else:
    st.error("File hero.jpg tidak ditemukan di folder assets/")


# ================= PROBLEM =================
st.markdown("## Permasalahan yang Dihadapi")

col1, col2 = st.columns([1, 1], gap="large")

with col1:
    st.markdown(
        """
        <p class="problem-text">
        Peningkatan jumlah penduduk dan aktivitas masyarakat di Kota Tasikmalaya 
        menyebabkan timbulan sampah terus meningkat dan berbeda pada setiap kecamatan. 
        Namun, data timbulan sampah yang tersedia masih dimanfaatkan secara historis 
        dan belum digunakan untuk mendukung perencanaan serta penentuan prioritas 
        penanganan sampah secara objektif. Kondisi ini berpotensi menyebabkan pengelolaan 
        sampah yang kurang efektif, sehingga diperlukan sistem prediksi timbulan sampah 
        berbasis data historis untuk membantu menentukan prioritas penanganan sampah secara lebih terukur.
        </p>
        """,
        unsafe_allow_html=True
    )

with col2:
    import os

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    img_path = os.path.join(BASE_DIR, "assets", "problem.png")

    if os.path.exists(img_path):
        st.image(img_path, use_container_width=True)
    else:
        st.warning("Gambar problem3.png tidak ditemukan")


# ================= SOLUTION =================
st.markdown(
    "<h2 style='text-align: center; margin-bottom: 2rem;'>Solusi yang Ditawarkan</h2>",
    unsafe_allow_html=True
)

c1, c2, c3 = st.columns(3)

def get_base64_img(path):
    if not os.path.exists(path):
        return ""
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

img1 = f"data:image/png;base64,{get_base64_img(os.path.join(BASE_DIR,'assets','solution1.png'))}"
img2 = f"data:image/png;base64,{get_base64_img(os.path.join(BASE_DIR,'assets','solution2.png'))}"
img3 = f"data:image/png;base64,{get_base64_img(os.path.join(BASE_DIR,'assets','solution3.png'))}"

with c1:
    st.markdown(f"""
        <div class="card-container">
            <img src="{img1}" class="card-img"/>
            <div class="card-content">
                <h3>Prediction & Analysis</h3>
                <p>
                Memprediksi jumlah timbulan sampah pada setiap kecamatan di Kota Tasikmalaya 
                berdasarkan data historis menggunakan metode Linear Regression.
                </p>
            </div>
        </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown(f"""
        <div class="card-container">
            <img src="{img2}" class="card-img"/>
            <div class="card-content">
                <h3>Priority Determination</h3>
                <p>
               Menentukan peringkat prioritas penanganan sampah pada setiap kecamatan berdasarkan 
               hasil prediksi timbulan sampah secara objektif dan terukur
                </p>
            </div>
        </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown(f"""
        <div class="card-container">
            <img src="{img3}" class="card-img"/>
            <div class="card-content">
                <h3>Decision Support System</h3>
                <p>
                Menyediakan sistem sederhana yang menampilkan hasil prediksi dan rekomendasi prioritas 
                penanganan sampah untuk mendukung pengambilan keputusan pemerintah daerah.
                </p>
            </div>
        </div>
    """, unsafe_allow_html=True)
    











