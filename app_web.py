import streamlit as st
from PIL import Image
import io

st.set_page_config(page_title="LSB Stealth", layout="wide", page_icon="🔐")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Instrument+Sans:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap');

*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

:root {
    --bg: #06060a;
    --surface: #0e0e16;
    --border: rgba(255,255,255,0.07);
    --text: #f0f0f8;
    --muted: #6b6b80;
}

html, body, .stApp {
    background: var(--bg) !important;
    font-family: 'Instrument Sans', sans-serif;
    color: var(--text);
}

header, footer, #MainMenu { visibility: hidden !important; }

/* NUKE ALL STREAMLIT PADDING/MARGIN */
.block-container { padding: 0 !important; max-width: 100% !important; margin: 0 !important; }
section[data-testid="stMain"] > div { padding: 0 !important; }
[data-testid="stVerticalBlock"] { gap: 0 !important; }
[data-testid="stAppViewBlockContainer"] { padding: 0 !important; max-width: 100% !important; }
div[data-testid="stVerticalBlockBorderWrapper"] { padding: 0 !important; }
.stTabs [data-baseweb="tab-panel"] { padding: 0 !important; }

/* ORBS */
.bg-orbs { position:fixed;inset:0;pointer-events:none;z-index:0;overflow:hidden; }
.orb { position:absolute;border-radius:50%;filter:blur(80px);animation:orbFloat ease-in-out infinite; }
.orb-1 { width:600px;height:600px;background:radial-gradient(circle,rgba(124,106,247,0.18) 0%,transparent 70%);top:-200px;left:-100px;animation-duration:10s; }
.orb-2 { width:500px;height:500px;background:radial-gradient(circle,rgba(192,132,252,0.14) 0%,transparent 70%);top:-100px;right:-150px;animation-duration:13s;animation-delay:-3s; }
.orb-3 { width:400px;height:400px;background:radial-gradient(circle,rgba(56,189,248,0.10) 0%,transparent 70%);bottom:20%;left:30%;animation-duration:15s;animation-delay:-6s; }
@keyframes orbFloat { 0%,100%{transform:translateY(0) scale(1);} 33%{transform:translateY(-30px) scale(1.05);} 66%{transform:translateY(20px) scale(0.97);} }

/* PAGE WRAPPER */
.page {
    position: relative; z-index: 2;
    width: 100%; max-width: 860px;
    margin-left: auto; margin-right: auto;
    padding: 0 32px 80px;
}

/* HERO */
.hero { padding: 80px 0 52px; text-align: center; }
.hero-pill { display:inline-flex;align-items:center;gap:8px;background:rgba(124,106,247,0.12);border:1px solid rgba(124,106,247,0.25);border-radius:100px;padding:8px 20px;font-size:0.75rem;font-weight:500;color:#a89bf8;margin-bottom:28px;animation:fadeUp 0.5s ease both; }
.pill-dot { width:6px;height:6px;background:#7c6af7;border-radius:50%;box-shadow:0 0 10px #7c6af7;animation:pulse 2s infinite; }
@keyframes pulse { 0%,100%{opacity:1;} 50%{opacity:0.3;} }
.hero-title { font-size:clamp(2.6rem,5.5vw,4.4rem);font-weight:700;line-height:1.05;letter-spacing:-2px;color:#fff;margin-bottom:18px;animation:fadeUp 0.5s 0.1s ease both; }
.grad { background:linear-gradient(135deg,#7c6af7 0%,#c084fc 50%,#38bdf8 100%);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text; }
.hero-sub { font-size:clamp(0.88rem,1.8vw,1rem);color:var(--muted);max-width:460px;margin:0 auto 20px;line-height:1.8;animation:fadeUp 0.5s 0.2s ease both;text-align:center !important;display:block; }
.hero-highlight { display:flex;align-items:center;justify-content:center;gap:12px;margin:0 auto 44px;flex-wrap:wrap;animation:fadeUp 0.5s 0.25s ease both; }
.hl-badge { display:inline-flex;align-items:center;gap:8px;padding:10px 20px;border-radius:12px;font-family:'JetBrains Mono',monospace;font-size:0.78rem;font-weight:500;letter-spacing:0.5px; }
.hl-badge-main { background:linear-gradient(135deg,rgba(124,106,247,0.2),rgba(192,132,252,0.15));border:1px solid rgba(124,106,247,0.4);color:#c4b8ff;box-shadow:0 0 20px rgba(124,106,247,0.15); }
.hl-badge-sec { background:rgba(255,255,255,0.04);border:1px solid var(--border);color:var(--muted); }
.hl-dot { width:7px;height:7px;border-radius:50%; }
.hl-dot-purple { background:#7c6af7;box-shadow:0 0 8px #7c6af7; }
.hl-dot-blue { background:#38bdf8;box-shadow:0 0 8px #38bdf8; }
@keyframes fadeUp { from{opacity:0;transform:translateY(18px);} to{opacity:1;transform:translateY(0);} }

/* FLOATING HEXAGONS */
.hex-wrap { position:relative;height:200px;margin:0 -32px 44px;overflow:hidden;animation:fadeUp 0.5s 0.25s ease both; }
.hex-wrap::before { content:'';position:absolute;inset:0;background:linear-gradient(to bottom,transparent 20%,var(--bg) 100%);z-index:2; }
.hex { position:absolute;border-radius:18px;animation:hexFloat ease-in-out infinite; }
.hex-1 { width:230px;height:230px;background:linear-gradient(135deg,#2d1b8e,#1a0f5e,#0d0730);border:1px solid rgba(124,106,247,0.3);box-shadow:0 0 60px rgba(124,106,247,0.15);left:10%;top:-10px;transform:rotate(-12deg);animation-duration:6s; }
.hex-2 { width:170px;height:170px;background:linear-gradient(135deg,#1a0f5e,#3d1b8e,#1a0f5e);border:1px solid rgba(192,132,252,0.25);left:40%;top:20px;transform:rotate(8deg);animation-duration:8s;animation-delay:-2s; }
.hex-3 { width:210px;height:210px;background:linear-gradient(135deg,#0d0730,#2d1b8e,#1e1060);border:1px solid rgba(56,189,248,0.2);right:8%;top:-5px;transform:rotate(18deg);animation-duration:7s;animation-delay:-4s; }
@keyframes hexFloat { 0%,100%{transform:translateY(0);} 50%{transform:translateY(-16px);} }

/* STATS */
.stats-row { display:flex;justify-content:center;flex-wrap:wrap;gap:1px;background:var(--border);border:1px solid var(--border);border-radius:16px;overflow:hidden;width:fit-content;margin:0 auto 52px;animation:fadeUp 0.5s 0.3s ease both; }
.stat { background:var(--surface);padding:15px 28px;text-align:center;transition:background 0.2s; }
.stat:hover { background:#1a1a28; }
.stat-val { font-size:1.4rem;font-weight:700;background:linear-gradient(135deg,#7c6af7,#c084fc);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;line-height:1; }
.stat-lbl { font-size:0.63rem;color:var(--muted);margin-top:4px;letter-spacing:0.5px; }

/* TABS */
.stTabs [data-baseweb="tab-list"] { background:var(--surface) !important;border-radius:14px !important;padding:5px !important;gap:4px !important;border:1px solid var(--border) !important;width:fit-content !important;margin:0 auto 0 !important;display:flex !important;justify-content:center !important; }
.stTabs [data-baseweb="tab"] { background:transparent !important;border-radius:10px !important;color:var(--muted) !important;font-family:'Instrument Sans',sans-serif !important;font-weight:500 !important;font-size:0.85rem !important;padding:10px 24px !important;border:none !important;height:auto !important; }
.stTabs [data-baseweb="tab"]:hover { color:#d0d0e8 !important; }
.stTabs [aria-selected="true"] { background:linear-gradient(135deg,rgba(124,106,247,0.2),rgba(192,132,252,0.15)) !important;color:#fff !important;border:1px solid rgba(124,106,247,0.3) !important;box-shadow:0 2px 16px rgba(124,106,247,0.15) !important; }
.stTabs [data-baseweb="tab-highlight"] { display:none !important; }

/* FEATURE STRIP — the key: everything block + text-align center on parent */
.feature-strip {
    display: block;
    width: 100%;
    text-align: center;
    padding: 36px 0 0;
    margin-bottom: 32px;
}
.feature-label {
    display: block;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.65rem; letter-spacing: 3px;
    text-transform: uppercase; color: rgba(124,106,247,0.5);
    margin-bottom: 10px;
}
.feature-title {
    display: block;
    font-size: clamp(1.8rem,4vw,2.6rem);
    font-weight: 700; color: #fff;
    letter-spacing: -1px; margin-bottom: 12px; line-height: 1.1;
}
.feature-desc {
    display: block;
    font-size: 0.9rem; color: var(--muted);
    max-width: 440px; margin: 0 auto 24px; line-height: 1.75;
}
.steps-row {
    display: flex;
    justify-content: center;
    align-items: center;
    flex-wrap: wrap;
    gap: 10px;
    margin-bottom: 20px;
}
.step-pill {
    display: inline-flex; align-items: center; gap: 10px;
    background: var(--surface); border: 1px solid var(--border);
    border-radius: 100px; padding: 9px 16px;
    font-size: 0.82rem; color: #8080a0;
    transition: all 0.2s; cursor: default;
}
.step-pill:hover { border-color:rgba(124,106,247,0.35);color:#c0c0e0;transform:translateY(-2px); }
.step-num { width:22px;height:22px;min-width:22px;background:rgba(124,106,247,0.15);border:1px solid rgba(124,106,247,0.3);border-radius:50%;display:flex;align-items:center;justify-content:center;font-family:'JetBrains Mono',monospace;font-size:0.6rem;color:#a89bf8;font-weight:700; }
.tags-row { display:flex;justify-content:center;flex-wrap:wrap;gap:8px;margin-bottom:28px; }
.tag { background:rgba(124,106,247,0.08);border:1px solid rgba(124,106,247,0.2);border-radius:8px;padding:5px 12px;font-family:'JetBrains Mono',monospace;font-size:0.65rem;color:#a89bf8;letter-spacing:1px; }

/* FORM CARD */
.form-card { background:var(--surface);border:1px solid var(--border);border-radius:24px;padding:36px 40px;position:relative;overflow:hidden;margin-bottom:8px; }
.form-card::before { content:'';position:absolute;top:0;left:0;right:0;height:1px;background:linear-gradient(90deg,transparent,rgba(124,106,247,0.6) 30%,rgba(192,132,252,0.6) 70%,transparent); }

.sec-title { font-size:0.72rem;font-weight:600;color:var(--muted);letter-spacing:1.5px;text-transform:uppercase;margin-bottom:16px;display:flex;align-items:center;gap:10px; }
.sec-title::after { content:'';flex:1;height:1px;background:var(--border); }

/* META */
.meta-box { background:var(--bg);border:1px solid var(--border);border-radius:14px;overflow:hidden;margin-top:8px; }
.meta-row { display:flex;justify-content:space-between;align-items:center;padding:11px 18px;border-bottom:1px solid var(--border); }
.meta-row:last-child { border-bottom:none; }
.meta-key { font-family:'JetBrains Mono',monospace;font-size:0.65rem;color:var(--muted);letter-spacing:1px; }
.meta-val { font-family:'JetBrains Mono',monospace;font-size:0.85rem;font-weight:500;color:#a89bf8; }

/* CAP BAR */
.cap-wrap { margin:20px 0; }
.cap-header { display:flex;justify-content:space-between;font-family:'JetBrains Mono',monospace;font-size:0.65rem;color:var(--muted);margin-bottom:8px; }
.cap-track { height:4px;background:rgba(255,255,255,0.05);border-radius:100px;overflow:hidden; }
.cap-fill { height:100%;border-radius:100px;transition:width 0.5s ease; }

/* UPLOADER */
.stFileUploader section { background:var(--bg) !important;border:1.5px dashed rgba(124,106,247,0.25) !important;border-radius:16px !important;padding:28px !important;transition:all 0.2s !important; }
.stFileUploader section:hover { border-color:rgba(124,106,247,0.5) !important;background:rgba(124,106,247,0.03) !important; }
.stFileUploader section p,.stFileUploader section span { color:var(--muted) !important;font-family:'Instrument Sans',sans-serif !important; }

/* TEXTAREA */
.stTextArea textarea { background:var(--bg) !important;border:1.5px solid var(--border) !important;border-radius:14px !important;color:var(--text) !important;font-family:'Instrument Sans',sans-serif !important;font-size:0.95rem !important;padding:16px 18px !important;transition:border-color 0.2s !important; }
.stTextArea textarea:focus { border-color:rgba(124,106,247,0.5) !important;box-shadow:0 0 0 3px rgba(124,106,247,0.08) !important; }
.stTextArea textarea::placeholder { color:rgba(107,107,128,0.4) !important; }
.stTextArea label,.stFileUploader label { color:var(--muted) !important;font-family:'Instrument Sans',sans-serif !important;font-weight:600 !important;font-size:0.78rem !important;letter-spacing:0.5px !important; }

/* BUTTONS */
.stButton > button { width:100% !important;background:linear-gradient(135deg,#7c6af7,#a855f7) !important;color:#fff !important;border:none !important;padding:15px 32px !important;border-radius:12px !important;font-family:'Instrument Sans',sans-serif !important;font-weight:600 !important;font-size:0.9rem !important;box-shadow:0 4px 24px rgba(124,106,247,0.3) !important;margin-top:10px !important;transition:all 0.25s ease !important; }
.stButton > button:hover { box-shadow:0 8px 32px rgba(124,106,247,0.45) !important;transform:translateY(-2px) !important; }
.stDownloadButton > button { width:100% !important;background:transparent !important;color:#a89bf8 !important;border:1px solid rgba(124,106,247,0.35) !important;padding:14px 32px !important;border-radius:12px !important;font-family:'Instrument Sans',sans-serif !important;font-weight:600 !important;font-size:0.9rem !important;margin-top:8px !important;transition:all 0.2s !important; }
.stDownloadButton > button:hover { background:rgba(124,106,247,0.1) !important;border-color:rgba(124,106,247,0.6) !important; }

/* ALERTS */
.stSuccess > div { background:rgba(16,185,129,0.08) !important;border:1px solid rgba(16,185,129,0.2) !important;border-radius:12px !important;color:#6ee7b7 !important; }
.stError > div { background:rgba(239,68,68,0.07) !important;border:1px solid rgba(239,68,68,0.2) !important;border-radius:12px !important;color:#fca5a5 !important; }
.stInfo > div { background:rgba(124,106,247,0.07) !important;border:1px solid rgba(124,106,247,0.2) !important;border-radius:12px !important;color:#c4b8ff !important; }
.stWarning > div { background:rgba(245,158,11,0.07) !important;border:1px solid rgba(245,158,11,0.2) !important;border-radius:12px !important;color:#fcd34d !important; }
.stImage > img { border-radius:14px !important;border:1px solid var(--border) !important; }

.result-box { background:var(--bg);border:1px solid var(--border);border-radius:14px;padding:22px 24px;font-family:'JetBrains Mono',monospace;font-size:0.85rem;color:#a89bf8;line-height:1.9;word-break:break-all;margin-top:12px; }

/* HOW */
.how-grid { display:grid;grid-template-columns:repeat(3,1fr);gap:16px;margin:24px 0; }
.how-card { background:var(--surface);border:1px solid var(--border);border-radius:20px;padding:26px 22px;transition:border-color 0.2s,transform 0.2s;position:relative;overflow:hidden; }
.how-card:hover { border-color:rgba(124,106,247,0.3);transform:translateY(-3px); }
.how-card::before { content:'';position:absolute;top:0;left:0;right:0;height:1px;background:linear-gradient(90deg,transparent,rgba(124,106,247,0.4),transparent);opacity:0;transition:opacity 0.3s; }
.how-card:hover::before { opacity:1; }
.how-num { font-family:'JetBrains Mono',monospace;font-size:0.62rem;color:rgba(124,106,247,0.4);letter-spacing:3px;margin-bottom:14px; }
.how-icon { font-size:1.6rem;margin-bottom:12px; }
.how-title { font-size:0.95rem;font-weight:700;color:#fff;margin-bottom:8px; }
.how-desc { font-size:0.8rem;color:var(--muted);line-height:1.7; }

.bit-demo { background:#030308;border:1px solid var(--border);border-radius:18px;padding:28px 32px;margin:20px 0;font-family:'JetBrains Mono',monospace; }
.bit-demo-label { font-size:0.62rem;letter-spacing:2px;color:var(--muted);text-transform:uppercase;margin-bottom:22px; }
.bit-grid { display:grid;grid-template-columns:1fr 1fr;gap:32px; }
.bit-col-title { font-size:0.62rem;letter-spacing:2px;color:rgba(107,107,128,0.5);text-transform:uppercase;margin-bottom:14px; }
.bit-row { font-size:0.82rem;color:#3a3a55;line-height:2.4; }
.bit-body { color:#4a4a70; }
.lsb-old { color:#f87171;font-weight:700; }
.lsb-new { color:#7c6af7;font-weight:700; }
.bit-note { margin-top:18px;padding-top:14px;border-top:1px solid var(--border);font-size:0.72rem;color:var(--muted); }

.warn-box { background:rgba(245,158,11,0.04);border:1px solid rgba(245,158,11,0.15);border-left:3px solid rgba(245,158,11,0.6);border-radius:14px;padding:20px 24px;margin-top:20px; }
.warn-title { font-weight:700;color:#fbbf24;font-size:0.9rem;margin-bottom:10px; }
.warn-box ul { padding-left:18px;color:#8a7040;font-size:0.82rem;line-height:2; }
.info-box { background:rgba(124,106,247,0.05);border:1px solid rgba(124,106,247,0.15);border-left:3px solid rgba(124,106,247,0.5);border-radius:14px;padding:18px 22px;font-size:0.88rem;color:#8080a0;line-height:1.8;margin-bottom:24px; }
.info-box strong { color:#a89bf8; }
.sdiv { border:none;border-top:1px solid var(--border);margin:26px 0; }
.footer { text-align:center;padding:48px 0 16px;font-size:0.72rem;color:#2a2a3a;letter-spacing:0.5px; }
.footer span { margin:0 8px; }
h3 { font-family:'Instrument Sans',sans-serif !important;color:#fff !important;font-weight:700 !important; }

/* MOBILE */
@media (max-width:768px) {
    .page { padding:0 16px 60px; }
    .hero { padding:56px 0 36px; }
    .how-grid { grid-template-columns:1fr; }
    .bit-grid { grid-template-columns:1fr;gap:20px; }
    .stats-row { width:100%; }
    .stat { padding:12px 16px;flex:1; }
    .form-card { padding:24px 20px; }
    .step-pill { width:100%;max-width:300px;justify-content:flex-start; }
    .hex-1 { left:2%;width:160px;height:160px; }
    .hex-2 { left:35%;width:120px;height:120px; }
    .hex-3 { right:2%;width:150px;height:150px; }
}
@media (max-width:480px) {
    .stats-row { flex-direction:column;width:100%; }
    .stat { border-right:none;border-bottom:1px solid var(--border); }
    .stat:last-child { border-bottom:none; }
    .steps-row { flex-direction:column;align-items:center; }
}
</style>

<div class="bg-orbs">
    <div class="orb orb-1"></div>
    <div class="orb orb-2"></div>
    <div class="orb orb-3"></div>
</div>
""", unsafe_allow_html=True)


def text_to_bin(text):
    return ''.join(format(ord(c), '08b') for c in text)

def max_capacity(img):
    img = img.convert('RGB')
    w, h = img.size
    return (w * h * 3 - 16) // 8

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
        if len(byte) < 8:
            break
        message += chr(int(byte, 2))
    return message


# HERO
st.markdown("""
<div class="page">
<div class="hero">
    <div class="hero-pill"><div class="pill-dot"></div>Kelompok 4 &nbsp;·&nbsp; Kriptografi & Keamanan Jaringan</div>
    <div class="hero-title">Sembunyikan Pesan,<br><span class="grad">Lindungi Privasi.</span></div>
    <span class="hero-sub">Sisipkan pesan rahasia ke dalam gambar tanpa mengubah tampilan visualnya sama sekali — menggunakan teknik kriptografi modern.</span>
    <div class="hero-highlight">
        <div class="hl-badge hl-badge-main"><div class="hl-dot hl-dot-purple"></div>LSB Steganography</div>
        <div class="hl-badge hl-badge-sec"><div class="hl-dot hl-dot-blue"></div>Least Significant Bit</div>
        <div class="hl-badge hl-badge-sec">🔐 Pixel-level Hiding</div>
    </div>
</div>
<div class="hex-wrap">
    <div class="hex hex-1"></div>
    <div class="hex hex-2"></div>
    <div class="hex hex-3"></div>
</div>
<div class="stats-row">
    <div class="stat"><div class="stat-val">1 bit</div><div class="stat-lbl">per channel RGB</div></div>
    <div class="stat"><div class="stat-val">3×</div><div class="stat-lbl">kapasitas piksel</div></div>
    <div class="stat"><div class="stat-val">PNG</div><div class="stat-lbl">output lossless</div></div>
    <div class="stat"><div class="stat-val">100%</div><div class="stat-lbl">lokal & privat</div></div>
</div>
""", unsafe_allow_html=True)

tab_enc, tab_dec, tab_info = st.tabs(["🔒  Encode", "🔓  Decode", "📖  Cara Kerja"])

# ENCODE
with tab_enc:
    st.markdown("""
    <div class="feature-strip">
        <span class="feature-label">// mode 01</span>
        <span class="feature-title">Encode &amp; <span class="grad">Sembunyikan</span></span>
        <span class="feature-desc">Upload gambar, tulis pesan, dan kami akan menyisipkannya ke dalam piksel menggunakan teknik LSB — hasilnya tidak bisa dibedakan secara visual.</span>
        <div class="steps-row">
            <div class="step-pill"><div class="step-num">01</div>Upload gambar sumber</div>
            <div class="step-pill"><div class="step-num">02</div>Tulis pesan rahasia</div>
            <div class="step-pill"><div class="step-num">03</div>Klik Encode</div>
            <div class="step-pill"><div class="step-num">04</div>Unduh PNG hasilnya</div>
        </div>
        <div class="tags-row">
            <span class="tag">INPUT: IMAGE + TEXT</span>
            <span class="tag">OUTPUT: STEGO PNG</span>
            <span class="tag">LOSSLESS</span>
            <span class="tag">INVISIBLE TO EYE</span>
        </div>
    </div>
    <div class="form-card">
    """, unsafe_allow_html=True)

    st.markdown('<div class="sec-title">Upload Gambar Sumber</div>', unsafe_allow_html=True)
    up_enc = st.file_uploader("Pilih gambar (PNG / JPG / JPEG)", type=["png","jpg","jpeg"], key="enc")

    if up_enc:
        img_obj = Image.open(up_enc)
        cap = max_capacity(img_obj)
        w, h = img_obj.size
        c1, c2 = st.columns([3, 2])
        with c1:
            st.image(up_enc, caption="Preview", use_container_width=True)
        with c2:
            st.markdown(f"""
            <div class="meta-box">
                <div class="meta-row"><span class="meta-key">Resolusi</span><span class="meta-val">{w} × {h}</span></div>
                <div class="meta-row"><span class="meta-key">Format</span><span class="meta-val">{img_obj.format or '—'}</span></div>
                <div class="meta-row"><span class="meta-key">Total piksel</span><span class="meta-val">{w*h:,}</span></div>
                <div class="meta-row"><span class="meta-key">Kapasitas maks</span><span class="meta-val">{cap:,} kar</span></div>
            </div>""", unsafe_allow_html=True)

        st.markdown('<hr class="sdiv"><div class="sec-title">Pesan Rahasia</div>', unsafe_allow_html=True)
        msg = st.text_area("Tulis pesan", placeholder="Ketik pesan yang ingin disembunyikan...", height=130)

        if msg:
            used = len(msg)
            pct = min(used / cap * 100, 100) if cap > 0 else 100
            color = "linear-gradient(90deg,#7c6af7,#a855f7)" if pct < 60 else ("linear-gradient(90deg,#f59e0b,#fbbf24)" if pct < 85 else "linear-gradient(90deg,#ef4444,#f87171)")
            st.markdown(f"""
            <div class="cap-wrap">
                <div class="cap-header"><span>Kapasitas terpakai</span><span>{used:,} / {cap:,} karakter ({pct:.1f}%)</span></div>
                <div class="cap-track"><div class="cap-fill" style="width:{pct}%;background:{color};"></div></div>
            </div>""", unsafe_allow_html=True)

        st.markdown('<hr class="sdiv"><div class="sec-title">Eksekusi</div>', unsafe_allow_html=True)
        if st.button("🔒  Encode & Sembunyikan Pesan", key="btn_enc"):
            if not msg:
                st.error("⚠️  Pesan tidak boleh kosong.")
            elif len(msg) > cap:
                st.error(f"⚠️  Pesan terlalu panjang. Maks {cap:,} karakter.")
            else:
                with st.spinner("Menyisipkan data ke piksel..."):
                    result = encode_logic(img_obj, msg)
                    buf = io.BytesIO()
                    result.save(buf, format="PNG")
                st.success("✅  Pesan berhasil disembunyikan!")
                st.info("💡  Bagikan file PNG aslinya — jangan screenshot atau kompres ulang.")
                st.download_button("⬇  Unduh Stego Image (PNG)", buf.getvalue(), "stego_output.png", mime="image/png")
    else:
        st.markdown('<div class="info-box"><strong>Tips:</strong> Gunakan gambar PNG beresolusi tinggi untuk kapasitas pesan yang lebih besar.</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

# DECODE
with tab_dec:
    st.markdown("""
    <div class="feature-strip">
        <span class="feature-label">// mode 02</span>
        <span class="feature-title">Decode &amp; <span class="grad">Ekstrak</span></span>
        <span class="feature-desc">Upload stego image yang kamu terima dan kami akan membaca bit LSB dari setiap piksel untuk memulihkan pesan tersembunyi di dalamnya.</span>
        <div class="steps-row">
            <div class="step-pill"><div class="step-num">01</div>Upload stego image (PNG asli)</div>
            <div class="step-pill"><div class="step-num">02</div>Klik Decode & Ekstrak</div>
            <div class="step-pill"><div class="step-num">03</div>Pesan tersembunyi tampil</div>
        </div>
        <div class="tags-row">
            <span class="tag">INPUT: STEGO IMAGE</span>
            <span class="tag">OUTPUT: TEXT</span>
            <span class="tag">READ-ONLY</span>
            <span class="tag">PNG ONLY</span>
        </div>
    </div>
    <div class="form-card">
    """, unsafe_allow_html=True)

    st.markdown('<div class="sec-title">Upload Stego Image</div>', unsafe_allow_html=True)
    up_dec = st.file_uploader("Upload gambar yang mengandung pesan", type=["png","jpg","jpeg"], key="dec")

    if up_dec:
        st.image(up_dec, caption="Stego Image", use_container_width=True)
        st.markdown('<hr class="sdiv"><div class="sec-title">Ekstrak Pesan</div>', unsafe_allow_html=True)
        if st.button("🔓  Decode & Ekstrak Pesan", key="btn_dec"):
            with st.spinner("Membaca bit LSB dari piksel..."):
                text = decode_logic(Image.open(up_dec))
            if text:
                st.success(f"✅  Pesan ditemukan — {len(text):,} karakter.")
                st.markdown("**Pesan Tersembunyi:**")
                st.markdown(f'<div class="result-box">{text}</div>', unsafe_allow_html=True)
            else:
                st.warning("⚠️  Tidak ada pesan ditemukan. Pastikan ini stego image valid.")
    else:
        st.markdown('<div class="info-box"><strong>Penting:</strong> Hanya gunakan file PNG asli dari encode. Screenshot atau gambar terkompresi akan merusak data tersembunyi.</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

# CARA KERJA
with tab_info:
    st.write("")
    st.markdown("""
    <div class="info-box"><strong>Apa itu Steganografi LSB?</strong><br>Steganografi menyembunyikan <em>keberadaan</em> pesan — bukan hanya isinya. Teknik <strong>LSB</strong> memanfaatkan bit paling kecil dari setiap channel warna piksel. Perubahan hanya ±1 sehingga tidak bisa dideteksi mata manusia.</div>
    <div class="how-grid">
        <div class="how-card"><div class="how-num">// 01</div><div class="how-icon">🔢</div><div class="how-title">Konversi ke Biner</div><div class="how-desc">Setiap karakter dikonversi ke 8-bit biner. 'A' → 01000001, 'Z' → 01011010</div></div>
        <div class="how-card"><div class="how-num">// 02</div><div class="how-icon">🎨</div><div class="how-title">Modifikasi LSB Piksel</div><div class="how-desc">Bit paling kanan dari R, G, B setiap piksel diganti dengan bit pesan. Perubahan hanya ±1.</div></div>
        <div class="how-card"><div class="how-num">// 03</div><div class="how-icon">🏁</div><div class="how-title">End Marker</div><div class="how-desc">Penanda akhir 16-bit ditambahkan agar decode tahu kapan harus berhenti membaca bit.</div></div>
    </div>
    <div class="bit-demo">
        <div class="bit-demo-label">// simulasi piksel — sebelum & sesudah encode</div>
        <div class="bit-grid">
            <div><div class="bit-col-title">// Sebelum (original)</div>
                <div class="bit-row">R = 200 → <span class="bit-body">1100100</span><span class="lsb-old">0</span></div>
                <div class="bit-row">G = 145 → <span class="bit-body">1001000</span><span class="lsb-old">1</span></div>
                <div class="bit-row">B = 78  → <span class="bit-body">0100111</span><span class="lsb-old">0</span></div>
            </div>
            <div><div class="bit-col-title">// Sesudah (encode '0','0','1')</div>
                <div class="bit-row">R = 200 → <span class="bit-body">1100100</span><span class="lsb-new">0</span></div>
                <div class="bit-row">G = 144 → <span class="bit-body">1001000</span><span class="lsb-new">0</span></div>
                <div class="bit-row">B = 79  → <span class="bit-body">0100111</span><span class="lsb-new">1</span></div>
            </div>
        </div>
        <div class="bit-note">G berubah 145→144, B berubah 78→79. Delta hanya ±1 — tidak dapat dibedakan secara visual.</div>
    </div>
    <div class="warn-box">
        <div class="warn-title">⚠ Keterbatasan Teknik LSB</div>
        <ul>
            <li>Rentan terhadap kompresi lossy (JPG/WEBP) — selalu gunakan PNG</li>
            <li>Dapat terdeteksi oleh alat steganalysis modern</li>
            <li>Tidak ada enkripsi — kombinasikan dengan kriptografi untuk keamanan lebih tinggi</li>
            <li>Kapasitas pesan terbatas pada resolusi gambar</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
<div class="footer">LSB Stealth <span>·</span> Kelompok 4 <span>·</span> Kriptografi & Keamanan Jaringan <span>·</span> 2025</div>
</div>
""", unsafe_allow_html=True)