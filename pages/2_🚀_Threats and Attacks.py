import json
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image
from streamlit_option_menu import option_menu

# Emojis: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(
    page_title="MELATI",
    page_icon=":blossom:",
    layout="wide"
)

# ---- LOCAL CSS ----
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

# Lottie Files: https://lottiefiles.com/
# ---- LOAD ASSETS ----
def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

lottie_thinking = load_lottiefile("./lottiefiles/cyber_thinking_2.json")
lottie_attacks_1 = load_lottiefile("./lottiefiles/cyber_threats_2.json")
lottie_attacks_2 = load_lottiefile("./lottiefiles/cyber_attacks_2.json")

# ---- SIDEBAR ----
with st.sidebar:
    st_lottie(lottie_thinking, height=200, key="thinking")

# ---- HORIZONTAL MENU ----
selected = option_menu(
    menu_title=None,
    options=["Cyber Threats", "Cyber Attacks"],
    icons=["bug", "hammer"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "#fafafa"},
        "icon": {"color": "orange", "font-size": "25px"},
        "nav-link": {
            "font-size": "25px",
            "text-align": "left",
            "margin": "0px",
            "--hover-color": "#eee",
        },
        "nav-link-selected": {"background-color": "green"},
    },
)

# ---- THREATS SECTION ----
if selected == "Cyber Threats":
    st.title("Cyber Threats")
    st.markdown("##")
    with st.container():
        left_column, right_column = st.columns(2)
        with left_column:
            st.write(
                """
                Cyber threats adalah setiap tindakan jahat yang mencoba untuk mendapatkan akses ke jaringan komputer tanpa izin atau izin dari pemiliknya.
                Ini mengacu pada berbagai aktivitas jahat yang dapat merusak atau mengganggu sistem komputer, jaringan, atau informasi yang dikandungnya.
                """
            )
            st.write("[Learn More >](https://www.upguard.com/blog/cyber-threat)")
        with right_column:
            image = Image.open("./images/cyber_threats.jpg")
            st.image(image)

    with st.container():
        st.write(
            """
            Threats dapat diklasifikasikan oleh beberapa kriteria:
            - Sumber daya penyerang.
            - Organisasi penyerang.
            - Dana penyerang.
            """
        )
        st.write("Atas dasar kriteria ini, threats terdiri dari 3 jenis:")
        tab1, tab2, tab3 = st.tabs(["Unstructured Cyber Threats", "Structured Cyber Threats", "Highly Structured Cyber Threats"])
        tab1.write(
            """
            - Sumber Daya: Individu atau Kelompok Kecil.
            - Organisasi: Sedikit atau tidak ada organisasi.
            - Pendanaan: Diabaikan.
            - Serangan: Mudah dideteksi dan memanfaatkan alat cyberattack yang tersedia secara bebas.
            - Eksploitasi berdasarkan kerentanan yang terdokumentasi.
            """
        )
        tab2.write(
            """
            - Sumber daya: Individu atau kelompok yang terlatih dengan baik.
            - Organisasi: Direncanakan dengan baik.
            - Pendanaan: Tersedia.
            - Serangan: Terhadap individu atau organisasi tertentu.
            - Eksploitasi berdasarkan pengumpulan informasi.
            """
        )
        tab3.write(
            """
            - Organisasi, sumber daya, dan perencanaan yang luas dari waktu ke waktu.
            - Serangan: Serangan jangka panjang pada mesin atau data tertentu.
            - Eksploitasi dengan banyak metode: bantuan teknis, sosial, dan orang dalam.
            """
        )

# ---- ATTACKS SECTION ----
if selected == "Cyber Attacks":
    st.title("Cyber Attacks")
    st.markdown("##")
    with st.container():
        left_column, right_column = st.columns(2)
        with left_column:
            st_lottie(lottie_attacks_1, height=300, key="attacks_1")
        with right_column:
            st.write(
                """
                Serangan dunia maya yang sukses dapat menyebabkan kerusakan besar pada organisasi atau sistem, serta reputasi bisnis dan kepercayaan konsumen.
                Beberapa hasil potensial meliputi:
                - Kerugian keuangan.
                - Kerusakan reputasi.
                - Konsekuensi hukum.
                """
            )
            st.write("[Learn More >](https://www.cisco.com/c/en/us/products/security/common-cyberattacks.html#~how-cyber-attacks-work)")

    with st.container():
        left_column, right_column = st.columns(2)
        with left_column:
            types = st.radio(
                "Types of cyber attacks:",
                ("Advanced Persistent Threat (APT)",
                "Backdoor",
                "Buffer Overflow",
                "Man-in-the-middle Attack",
                "Cross-Site Scripting (XSS)",
                "Denial of Service Attack",
                "SQL Injection",
                "Zero-day Exploit"))
        with right_column:
            if types == "Advanced Persistent Threat (APT)":
                st.info("Serangan jaringan di mana orang yang tidak sah mendapatkan akses ke jaringan dan tetap di sana tidak terdeteksi untuk jangka waktu yang lama.")
            elif types == "Backdoor":
                st.info("Metode melewati otentikasi normal dan mendapatkan akses dalam OS atau aplikasi.")
            elif types == "Buffer Overflow":
                st.info("Eksploitasi yang memanfaatkan program yang sedang menunggu input pengguna.")
            elif types == "Man-in-the-middle Attack":
                st.info("Serangan ini mencegat dan menyampaikan pesan antara dua pihak yang berkomunikasi langsung satu sama lain.")
            elif types == "Cross-Site Scripting (XSS)":
                st.info("Serangan injeksi kode yang memungkinkan penyerang untuk menjalankan javascript berbahaya di browser pengguna lain.")
            elif types == "Denial of Service Attack":
                st.info("Setiap serangan di mana para penyerang berusaha mencegah pengguna yang berwenang mengakses layanan.")
            elif types == "SQL Injection":
                st.info("Kerentanan aplikasi web yang sangat umum dieksploitasi yang memungkinkan peretas jahat mencuri dan mengubah data dalam database situs web.")
            elif types == "Zero-day Exploit":
                st.info("Kerentanan dalam sistem atau perangkat yang telah diungkapkan tetapi belum ditambal.")
            st_lottie(lottie_attacks_2, height=300, key="attacks_2")