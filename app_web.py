import streamlit as st
from PIL import Image
import io

# --- KONFIGURASI HALAMAN ---
st.set_page_config(page_title="LSB Stealth", layout="wide")

# --- CUSTOM CSS: SKY BLUE MINIMALIST ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@300;400;500;600&family=Syne:wght@700;800&display=swap');

    *, *::before, *::after { box-sizing: border-box; }

    html, body, .stApp {
        background-color: #f0f8ff;
        font-family: 'DM Sans', sans-serif;
        color: #1a2e44;
    }

    header, footer { visibility: hidden !important; }
    #MainMenu { visibility: hidden !important; }
    .block-container {
        padding-top: 2rem !important;
        padding-bottom: 2rem !important;
        max-width: 900px !important;
    }

    .stApp::before {
        content: '';
        position: fixed;
        top: -200px; right: -200px;
        width: 600px; height: 600px;
        background: radial-gradient(circle, rgba(56, 182, 255, 0.15) 0%, transparent 70%);
        border-radius: 50%;
        pointer-events: none;
        z-index: 0;
    }

    .stApp::after {
        content: '';
        position: fixed;
        bottom: -150px; left: -150px;
        width: 500px; height: 500px;
        background: radial-gradient(circle, rgba(14, 165, 233, 0.1) 0%, transparent 70%);
        border-radius: 50%;
        pointer-events: none;
        z-index: 0;
    }

    .hero-badge {
        display: inline-block;
        background: rgba(14, 165, 233, 0.1);
        border: 1px solid rgba(14, 165, 233, 0.25);
        color: #0284c7;
        font-size: 0.7rem;
        font-weight: 600;
        letter-spacing: 3px;
        text-transform: uppercase;
        padding: 6px 18px;
        border-radius: 100px;
        margin-bottom: 20px;
    }

    .main-title {
        font-family: 'Syne', sans-serif;
        font-weight: 800;
        font-size: 3.8rem;
        line-height: 1.05;
        letter-spacing: -2px;
        color: #0c1d2e;
        margin-bottom: 12px;
    }

    .main-title span { color: #0ea5e9; }

    .subtitle {
        font-size: 1rem;
        color: #5a7a99;
        font-weight: 400;
        margin-bottom: 50px;
    }

    .card {
        background: #ffffff;
        border: 1px solid rgba(14, 165, 233, 0.15);
        border-radius: 24px;
        padding: 40px 44px;
        box-shadow: 0 4px 40px rgba(14, 165, 233, 0.07), 0 1px 3px rgba(0,0,0,0.04);
        position: relative;
        overflow: hidden;
    }

    .card::before {
        content: '';
        position: absolute;
        top: 0; left: 0; right: 0;
        height: 3px;
        background: linear-gradient(90deg, #38bdf8, #0ea5e9, #0284c7);
        border-radius: 24px 24px 0 0;
    }

    .stTabs [data-baseweb="tab-list"] {
        background: #f0f8ff !important;
        border-radius: 14px !important;
        padding: 5px !important;
        gap: 4px !important;
        border: 1px solid rgba(14, 165, 233, 0.15) !important;
        width: fit-content !important;
        margin: 0 auto 32px !important;
    }

    .stTabs [data-baseweb="tab"] {
        background: transparent !important;
        border-radius: 10px !important;
        color: #5a7a99 !important;
        font-family: 'DM Sans', sans-serif !important;
        font-weight: 500 !important;
        font-size: 0.88rem !important;
        letter-spacing: 0.5px !important;
        padding: 10px 28px !important;
        border: none !important;
        height: auto !important;
    }

    .stTabs [aria-selected="true"] {
        background: #0ea5e9 !important;
        color: #ffffff !important;
        box-shadow: 0 2px 12px rgba(14, 165, 233, 0.3) !important;
    }

    .stTabs [data-baseweb="tab-highlight"] { display: none !important; }

    .stFileUploader section {
        background: #f7fbff !important;
        border: 2px dashed rgba(14, 165, 233, 0.3) !important;
        border-radius: 16px !important;
        padding: 24px !important;
    }

    .stFileUploader section:hover {
        border-color: #0ea5e9 !important;
    }

    .stFileUploader section p, .stFileUploader section span {
        color: #5a7a99 !important;
        font-family: 'DM Sans', sans-serif !important;
    }

    .stTextArea textarea {
        background: #f7fbff !important;
        border: 1.5px solid rgba(14, 165, 233, 0.2) !important;
        border-radius: 14px !important;
        color: #1a2e44 !important;
        font-family: 'DM Sans', sans-serif !important;
        font-size: 0.95rem !important;
        padding: 14px 18px !important;
    }

    .stTextArea textarea:focus {
        border-color: #0ea5e9 !important;
        box-shadow: 0 0 0 3px rgba(14, 165, 233, 0.1) !important;
    }

    .stTextArea textarea::placeholder { color: #9db8cc !important; }

    .stTextArea label, .stFileUploader label {
        color: #2d4a63 !important;
        font-family: 'DM Sans', sans-serif !important;
        font-weight: 600 !important;
        font-size: 0.88rem !important;
        letter-spacing: 0.5px !important;
        text-transform: uppercase !important;
    }

    .stButton > button {
        width: 100% !important;
        background: #0ea5e9 !important;
        color: #ffffff !important;
        border: none !important;
        padding: 14px 28px !important;
        border-radius: 12px !important;
        font-family: 'DM Sans', sans-serif !important;
        font-weight: 600 !important;
        font-size: 0.88rem !important;
        letter-spacing: 1.5px !important;
        text-transform: uppercase !important;
        box-shadow: 0 2px 16px rgba(14, 165, 233, 0.25) !important;
        margin-top: 8px !important;
        transition: all 0.25s ease !important;
    }

    .stButton > button:hover {
        background: #0284c7 !important;
        box-shadow: 0 6px 24px rgba(14, 165, 233, 0.4) !important;
        transform: translateY(-2px) !important;
    }

    .stDownloadButton > button {
        width: 100% !important;
        background: transparent !important;
        color: #0ea5e9 !important;
        border: 1.5px solid #0ea5e9 !important;
        padding: 13px 28px !important;
        border-radius: 12px !important;
        font-family: 'DM Sans', sans-serif !important;
        font-weight: 600 !important;
        font-size: 0.88rem !important;
        letter-spacing: 1.5px !important;
        text-transform: uppercase !important;
        margin-top: 6px !important;
        transition: all 0.25s ease !important;
    }

    .stDownloadButton > button:hover {
        background: #0ea5e9 !important;
        color: #ffffff !important;
    }

    .stSuccess {
        background: rgba(16, 185, 129, 0.08) !important;
        border: 1px solid rgba(16, 185, 129, 0.25) !important;
        border-radius: 12px !important;
    }

    .stError {
        background: rgba(239, 68, 68, 0.07) !important;
        border: 1px solid rgba(239, 68, 68, 0.2) !important;
        border-radius: 12px !important;
    }

    .stInfo {
        background: rgba(14, 165, 233, 0.07) !important;
        border: 1px solid rgba(14, 165, 233, 0.2) !important;
        border-radius: 12px !important;
        color: #0c4a6e !important;
    }

    .stImage > img {
        border-radius: 16px !important;
        border: 1px solid rgba(14, 165, 233, 0.15) !important;
        margin: 12px 0 !important;
    }

    .section-divider {
        border: none;
        border-top: 1px solid rgba(14, 165, 233, 0.1);
        margin: 28px 0;
    }

    h3 {
        font-family: 'Syne', sans-serif !important;
        color: #0c1d2e !important;
        font-size: 1.1rem !important;
    }

    .footer {
        text-align: center;
        color: #9db8cc;
        font-size: 0.78rem;
        letter-spacing: 2px;
        text-transform: uppercase;
        padding: 24px 0 8px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- LOGIKA ---
def text_to_bin(text):
    return ''.join(format(ord(i), '08b') for i in text)

def encode_logic(img, secret_data):
    binary_msg = text_to_bin(secret_data) + '1111111111111110'
    data_index = 0
    img = img.convert('RGB')
    pixels = list(img.getdata())
    new_pixels = []
    for pixel in pixels:
        pixel = list(pixel)
        for i in range(3):
            if data_index < len(binary_msg):
                pixel[i] = pixel[i] & ~1 | int(binary_msg[data_index])
                data_index += 1
        new_pixels.append(tuple(pixel))
    new_img = Image.new(img.mode, img.size)
    new_img.putdata(new_pixels)
    return new_img

def decode_logic(img):
    img = img.convert('RGB')
    pixels = list(img.getdata())
    binary_msg = ""
    for pixel in pixels:
        for i in range(3):
            binary_msg += str(pixel[i] & 1)
    end_marker = "1111111111111110"
    if end_marker in binary_msg:
        binary_msg = binary_msg[:binary_msg.index(end_marker)]
    message = ""
    for i in range(0, len(binary_msg), 8):
        byte = binary_msg[i:i+8]
        if len(byte) < 8: break
        message += chr(int(byte, 2))
    return message

# --- UI ---
st.markdown("""
    <div style="text-align: center; padding: 20px 0 40px;">
        <div class="hero-badge">Kelompok 4 &nbsp;·&nbsp; Kriptografi</div>
        <div class="main-title">LSB <span>Stealth</span></div>
        <p class="subtitle">Sembunyikan pesan rahasia di dalam gambar menggunakan teknik Least Significant Bit</p>
    </div>
""", unsafe_allow_html=True)

_, center, _ = st.columns([1, 10, 1])

with center:
    tab1, tab2 = st.tabs(["🔒  ENCODE", "🔓  DECODE"])

    with tab1:
        st.write("")
        up_enc = st.file_uploader("Pilih gambar sumber", type=["png","jpg","jpeg"], key="enc")
        if up_enc:
            st.image(up_enc, caption="Pratinjau Gambar", use_container_width=True)
            st.markdown('<hr class="section-divider">', unsafe_allow_html=True)
            msg = st.text_area("Pesan Rahasia", placeholder="Tulis pesan yang ingin disembunyikan...", height=120)
            if st.button("PROSES & SEMBUNYIKAN"):
                if msg:
                    with st.spinner('Menyembunyikan data ke dalam piksel...'):
                        res = encode_logic(Image.open(up_enc), msg)
                        buf = io.BytesIO()
                        res.save(buf, format="PNG")
                        st.success("✓  Pesan berhasil disembunyikan dalam gambar.")
                        st.download_button("↓  UNDUH HASIL", buf.getvalue(), "stego_output.png")
                else:
                    st.error("Pesan tidak boleh kosong.")

    with tab2:
        st.write("")
        up_dec = st.file_uploader("Unggah Stego Image", type=["png","jpg","jpeg"], key="dec")
        if up_dec:
            st.image(up_dec, caption="Gambar yang Diunggah", use_container_width=True)
            st.markdown('<hr class="section-divider">', unsafe_allow_html=True)
            if st.button("EKSTRAK PESAN"):
                with st.spinner('Membaca piksel dan memulihkan pesan...'):
                    text = decode_logic(Image.open(up_dec))
                    st.markdown("### 📩 Pesan Tersembunyi")
                    st.info(text if text else "Tidak ada pesan yang ditemukan dalam gambar ini.")

st.markdown('<div class="footer">Secure Data Hiding System &nbsp;·&nbsp; LSB Steganography</div>', unsafe_allow_html=True)