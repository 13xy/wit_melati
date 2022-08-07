import streamlit as st # pip install streamlit
import json # pip install jsons
from streamlit_lottie import st_lottie # pip install streamlit-lottie
from PIL import Image # pip install Pillow
from streamlit_option_menu import option_menu # pip install streamlit-option-menu

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

lottie_team = load_lottiefile("./lottiefiles/cyber_team.json")

# ---- LOAD ANIMATION ----
animation_symbol = "❄"

st.markdown(
    f"""
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    """,
    unsafe_allow_html=True,
)

# ---- SIDEBAR ----
with st.sidebar:
    st_lottie(lottie_team, height=200, key="team")

# ---- ABOUT US ----
st.markdown("<h1 style='text-align: center; color: deeppink;'>ABOUT US</h1>", unsafe_allow_html=True)
st.markdown("##")
st.header("We are Team Melati")
st.write("##")
st.write("Perkenalkan, kami dari team Melati.")
st.write(
    """
    Awal mula kami bertemu adalah secara online di pelatihan Women in Tech: Cybersecurity and Python Periode 4 Juli - 8 Agustus 2022.
    Pada Thematic Academy yang diselenggarakan oleh Tim Digital Talent Scholarship, Kementerian Komunikasi dan Informatika Republik Indonesia, kami berada dalam kelas yang sama, yaitu kelas S.
    Di kelas yang terdiri dari 64 orang perempuan-perempuan hebat ini pun awalnya kami hanya saling mengenal nama saja.
    Setelah belajar bersama-sama selama lebih dari dua minggu, akhirnya pada 20 Juli 2022, kami dipersatukan menjadi satu kelompok untuk pembuatan Final Project Hackathon menggunakan bahasa pemrograman Python dan pengetahuan cybersecurity.
    Kelompok nomor 15 yang kami beri nama Melati ini terdiri dari Kushartanti Alifah, Ani Siti Fatimah, dan Stella Sumarli.
    Sesuai dengan nama team Melati, yang diambil dari nama bunga Melati sebagai puspa bangsa, kami berharap agar kelompok kami dapat menjadi salah satu perwakilan perempuan-perempuan Indonesia yang hebat di bidang teknologi nasional dan dunia.
    """
)

with st.container():
    st.write("---")
    st.header("Our People")
    st.write("##")
    left_column, middle_column, right_column = st.columns(3)
    with left_column:
        image1 = Image.open("./images/tanti.jpg")
        st.image(image1, caption="Kushartanti Alifah")
    with middle_column:
        image2 = Image.open("./images/second.jpg")
        st.image(image2, caption="Ani Siti Fatimah")
    with right_column:
        image_stella = Image.open("./images/stella.jpg")
        st.image(image_stella, caption="Stella Sumarli")

# ---- HORIZONTAL MENU ----
selected = option_menu(
    menu_title=None,
    options=["TANTI", "ANI", "STELLA"],
    icons=["emoji-sunglasses", "emoji-heart-eyes", "emoji-wink"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "#fafafa"},
        "icon": {"color": "green", "font-size": "25px"},
        "nav-link": {
            "font-size": "25px",
            "text-align": "left",
            "margin": "0px",
            "--hover-color": "#eee",
        },
        "nav-link-selected": {"background-color": "deeppink"},
    },
)

# ---- TANTI ----
if selected == "TANTI":
    st.subheader("Hi, I am Kushartanti Alifah :wave:")
    st.markdown("##")
    st.write("[LinkedIn >](http://linkedin.com/in/kushartanti-alifah)")

# ---- ANI ----
if selected == "ANI":
    st.subheader("Hi, I am Ani Siti Fatimah :wave:")
    st.markdown("##")

# ---- STELLA ----
if selected == "STELLA":
    st.subheader("Hi, I am Stella Sumarli :wave:")
    st.markdown("##")
    st.write(
        """
        Saya sangat menyukai tentang semua hal yang berkaitan tentang bidang teknologi komputer.
        Walaupun saya mempunyai latar belakang pendidikan di bidang teknologi komputer, tetapi saya belum pernah mempelajari mengenai bahasa pemrograman Python secara khusus dan resmi.
        Oleh karena itu, saya sangat senang sekali saat mengetahui bahwa saya terpilih menjadi salah satu peserta Pelatihan Women in Tech: Cybersecurity and Python Periode 4 Juli - 8 Agustus 2022.
        Pelatihan ini sangat membantu saya mempelajari algoritma pemrograman, library, dan syntax dari Python.
        Selain itu, pada bagain kedua saya juga mempelajari cybersecurity dari tingkat dasar (literasi).
        Pengetahuan tentang cybersecurity ini sangat membantu saya untuk memahami macam-macam cyber attack dalam kehidupan sehari-hari, serta cara untuk menghindarinya.
        """
    )
    st.write(
        """
        Terkait cybersecurity di kehidupan sehari-hari, saya pernah menyaksikan pengalaman salah seorang rekan kerja saya dalam menghadapi cyber attack di tempat kerja.
        Beberapa tahu yang lalu, rekan kerja saya pernah terkena cyber attack melalui email, yang sering disebut sebagai phishing.
        Beliau mendapatkan email yang berisikan subjek terkait perkerjaan.
        Setelah email tersebut dibuka, secara otomatis data yang ada di komputer yang dipakai untuk membuka email tersebut langsung tidak bisa diakses kembali.
        Di email tersebut disebutkan apabila kami masih ingin mendapatkan data-data berharga tersebut, kami harus mengikuti arahan mereka dengan memberikan sejumlah uang.
        Pada awalnya, rekan kerja saya tersebut merasa panik dan bersalah karena sudah membuka email secara ceroboh dan kurang hati-hati.
        Kemudian beliau melaporkan kejadian tersebut ke atasan kami.
        Setelah menjelaskan rincian kejadiannya, atasan kami melaporkan ke kantor pusat.
        Dan setelah melalui berbagai diskusi dan pertimbangan yang panjang, kantor pusat membantu untuk menyelesaikan masalah tersebut.
        """
    )
    st.write("[LinkedIn >](https://www.linkedin.com/in/stella-sumarli-35b0ba18b)")

# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Get In Touch With Us")
    st.write("##")
    
    # Documention: https://formsubmit.co/
    contact_form = """
    <form action="https://formsubmit.co/stella.sumarli@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()