import streamlit as st
from PIL import Image
import io

# --- KONFIGURASI HALAMAN ---
st.set_page_config(page_title="LSB Stealth", page_icon="🕵️", layout="wide")

# --- CUSTOM CSS: CYBER STEALH UI ---
st.markdown("""
    <style>
    /* Import Font Modern & Tech */
    @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;500;700&display=swap');

    /* Background Utama Gelap Total */
    .stApp {
        background-color: #05070a;
        font-family: 'Space Grotesk', sans-serif;
        color: #e0e0e0;
    }

    /* Hilangkan Header Default Streamlit */
    header {visibility: hidden;}
    
    /* Main Container / Panel Kaca */
    .glass-panel {
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 30px;
        padding: 40px;
        margin-top: -50px;
        box-shadow: 0 25px 50px rgba(0,0,0,0.5);
    }

    /* Judul Stealth */
    .main-title {
        font-weight: 700;
        font-size: 3.5rem;
        letter-spacing: -2px;
        background: linear-gradient(90deg, #00f2ff, #0072ff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 5px;
    }

    /* Tombol Bergaya Modern */
    .stButton>button {
        width: 100%;
        background: #00f2ff;
        color: #000 !important;
        border: none;
        padding: 15px;
        border-radius: 12px;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 1px;
        transition: 0.4s;
    }

    .stButton>button:hover {
        background: #ffffff;
        box-shadow: 0 0 30px rgba(0, 242, 255, 0.4);
        transform: translateY(-3px);
    }

    /* Style Input & Text Area */
    .stTextArea textarea, .stFileUploader section {
        background-color: rgba(255,255,255,0.05) !important;
        border: 1px solid rgba(255,255,255,0.1) !important;
        border-radius: 15px !important;
        color: white !important;
    }

    /* Styling Tab agar tidak kaku */
    .stTabs [data-baseweb="tab-list"] {
        gap: 20px;
        justify-content: center;
        background-color: transparent;
    }
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        background-color: rgba(255,255,255,0.05);
        border-radius: 10px;
        color: #888;
        border: none;
        padding: 0 30px;
    }
    .stTabs [aria-selected="true"] {
        background-color: #00f2ff !important;
        color: #000 !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- LOGIKA ASLI (TETAP SAMA) ---
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

# --- UI CONTENT ---
st.markdown('<h1 class="main-title">STEALTH LSB.</h1>', unsafe_allow_html=True)
st.markdown('<p style="text-align:center; color:#666; margin-bottom:50px;">PROYEK KRIPTOGRAFI KELOMPOK 4</p>', unsafe_allow_html=True)

# Main Container
_, center, _ = st.columns([1, 6, 1])

with center:
    st.markdown('<div class="glass-panel">', unsafe_allow_html=True)
    
    tab1, tab2 = st.tabs(["🔒 ENCODE", "🔓 DECODE"])

    with tab1:
        st.write("##")
        up_enc = st.file_uploader("Upload Image (PNG)", type=["png"], key="enc")
        if up_enc:
            st.image(up_enc, caption="Source Image", use_container_width=True)
            msg = st.text_area("Pesan Rahasia:", placeholder="Masukkan pesan rahasia di sini...")
            
            if st.button("PROCESS & HIDE"):
                if msg:
                    with st.spinner('Hiding data...'):
                        res = encode_logic(Image.open(up_enc), msg)
                        buf = io.BytesIO()
                        res.save(buf, format="PNG")
                        st.success("Data hidden successfully!")
                        st.download_button("DOWNLOAD RESULT", buf.getvalue(), "stego.png")
                else:
                    st.error("Isi pesan dulu!")

    with tab2:
        st.write("##")
        up_dec = st.file_uploader("Upload Stego Image", type=["png"], key="dec")
        if up_dec:
            st.image(up_dec, use_container_width=True)
            if st.button("EXTRACT MESSAGE"):
                with st.spinner('Reading pixels...'):
                    text = decode_logic(Image.open(up_dec))
                    st.markdown("### 📩 Hasil Ekstraksi:")
                    st.info(text if text else "Pesan tidak ditemukan.")

    st.markdown('</div>', unsafe_allow_html=True)

# Footer Minimalis
st.markdown("<br><p style='text-align: center; color: #333;'>SECURE DATA HIDING SYSTEM</p>", unsafe_allow_html=True)