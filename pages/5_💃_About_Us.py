import streamlit as st # pip install streamlit
import json # pip install jsons
from streamlit_lottie import st_lottie # pip install streamlit-lottie
from PIL import Image # pip install Pillow

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
st.markdown("##")
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
    st.markdown("##")
    left_column, middle_column, right_column = st.columns(3)
    with left_column:
        image1 = Image.open("./images/tanti.jpg")
        st.image(image1, caption="Kushartanti Alifah")
        st.write("[LinkedIn >](http://linkedin.com/in/kushartanti-alifah)")
    with middle_column:
        image2 = Image.open("./images/ani.jpeg")
        new_image2 = image2.resize((400, 400))
        st.image(new_image2, caption="Ani Siti Fatimah")
        st.write("[Instagram >](https://instagram.com/anistf_22?igshid=YmMyMTA2M2Y=)")
    with right_column:
        image_stella = Image.open("./images/stella.jpg")
        st.image(image_stella, caption="Stella Sumarli")
        st.write("[LinkedIn >](https://www.linkedin.com/in/stella-sumarli-35b0ba18b)")

with st.container():
    st.write("---")
    st.header("Our Experience")
    st.markdown("##")
    st.write(
        """
        1. Aplikasi discord -> tipe penyerangan pishing and scamming.
            Kronologi ada user discord yang berada dalam satu server yang sama dan mengirimkan chat spamming kepada setiap user yang berada di server itu.
            Nah di dalam chat nya seperti berikut ini, ex : FREE GIVEAWAY lalu ada URL (disc0rd.gg/free).
            Link URL dibuat menyerupai URL asli dari discord yaitu (discord.gg).
            Setelah korban mengklik URL tersebut maka diarahkan ke dalam web dan dimintai untuk memasukkan password.
            Setelah korban memasukkan password dan email maka saat itu juga akun korban sudah pindah tangan kepada tersangka.
            Yang di mana tersangka ini menggunakan akun korban, sama seperti akun yang lain yaitu melakukan chat spamming yang berisi link phising dan scam.
        2. Free bitcoin -> tipe penyerangan scamming.
            Kronologi terdapat suatu web yang di mana kita melakukan sign in kita akan mendapatkan free bitcoin dan juga mendapatkan 1 mode mining yang di mana terdapat banyak mode mining.
            Namun untuk menggunakan mode mining lainnya kita perlu membayar.
            Untuk kecepatan mode mining yang free sangatlah lambat dibandingkan dengan yang berbayar.
            Lalu ada user yang terkena scam dengan melakukan deposito dan membeli mode mining yang tercepat dengan total kerugian 400.000.
            Setelah membeli memang benar mode mining tersebut langsung bisa digunakan.
            Namun dalam kurun waktu 1 minggu, website tersebut tidak bisa diakses kembali.
            Maka uang yang telah dideposito kan ke website tersebut hilang dan terjadi scamming dari pelaku kepada user korban.
        """
    )
    st.subheader("Solution:")
    st.write(
        """
        1. Lakukan password recovery via email.
        2. Aktifkan 2FA(two factor authentication).
        3. Unlink all device yang telah login.
        4. Laporkan ke pihak yang berwenang, yang mampu menangani cyber attack dengan sigap dan tanggap.
        5. Relakan (Sudah tidak bisa balik lagi).
        """
    )
    st.subheader("Prevention:")
    st.write(
        """
        1. Memperbarui software.
        2. Gunakan password yang kuat dan unik.
        3. Backup data.
        4. Aktifkan 2FA.
        5. Gunakan VPN saat melakukan koneksi melalui wifi publik.
        """
    )

# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Get In Touch With Us")
    st.markdown("##")
    
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