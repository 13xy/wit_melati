import json
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image

st.set_page_config(
    page_title="MELATI",
    page_icon=":blossom:",
    layout="wide"
)

# ---- LOAD ASSETS ----
def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

lottie_thanks = load_lottiefile("./lottiefiles/cyber_thanks_4.json")

# ---- SIDEBAR ----
with st.sidebar:
    if st.button("Thank You"):
        st.success(
            """
            Team Melati :
            - Kushartanti Alifah
            - Ani Siti Fatimah
            - Stella Sumarli
            """
        )
        st_lottie(lottie_thanks, height=200, key="thanks")

st.title("Conclusion")

with st.container():
    left_column, right_column = st.columns(2)
    with left_column:
        st.write(
            """
            Lima topik yang perlu dipertimbangkan untuk melindungi diri Anda dari serangan cyber yang paling umum.
            Ini mudah diterapkan, berbiaya rendah, dan dapat membantu mencegah insiden kecil dan besar.
            """
        )
        with st.expander("Protect your data"):
            st.write(
                """
                - Amankan semua perangkat Anda menggunakan perlindungan kata sandi atau PIN.
                - Gunakan kata sandi yang kuat, atur ulang bila diperlukan, dan ubah kata sandi default.
                - Gunakan otentikasi multi-faktor jika tersedia.
                Ini memberikan lapisan keamanan tambahan ke akun Anda dengan mengonfirmasi identitas pengguna.
                """
            )
        with st.expander("Prevent malware"):
            st.write(
                """
                - Pastikan perangkat lunak anti-virus Anda dihidupkan, selalu diperbarui, dan lakukan pemindaian sistem secara teratur.
                - Jangan mengunduh atau menginstal perangkat lunak dan aplikasi pihak ketiga dari sumber yang tidak dikenal.
                - Dorong staf untuk hanya mentransfer file melalui jaringan, melalui email atau penyimpanan cloud yang aman, daripada media yang dapat dipindahkan.
                - Patch perangkat lunak secara teratur, dan atur perangkat lunak untuk diperbarui secara otomatis, jika memungkinkan. Selalu aktifkan firewall Anda.
                """
            )
        with st.expander("Avoid phishing attacks"):
            st.write(
                """
                - Jangan menjelajahi web atau menggunakan email di akun dengan hak administrator.
                - Lakukan pemindaian anti-virus untuk malware dan ubah kata sandi jika Anda mencurigai atau mengidentifikasi serangan atau akun yang disusupi.
                - Apakah alamat email pengirim sah? Apakah email tersebut tidak terduga atau mencurigakan?
                """
            )
        with st.expander("Backup your data"):
            st.write(
                """
                - Pertimbangkan pencadangan lengkap sistem dan data, tetapi jika ini tidak praktis, putuskan data apa yang dibutuhkan organisasi Anda untuk tetap berjalan dan seberapa sering data ini harus dicadangkan.
                - Simpan cadangan Anda di lokasi yang berbeda dengan data asli Anda - pertimbangkan untuk menggunakan cloud.
                """
            )
        with st.expander("Keep your devices safe"):
            st.write(
                """
                - Lindungi perangkat Anda menggunakan kata sandi/PIN/pengenalan sidik jari.
                - Siapkan pelacakan perangkat dan penghapusan jarak jauh untuk mencegah data Anda disusupi jika perangkat Anda hilang.
                - Selalu perbarui semua perangkat dan aplikasi Anda.
                - Gunakan data seluler (3/4/5G), daripada menyambung ke hotspot Wi-Fi publik saat mengirim atau menerima data sensitif.
                - Perangkat kedaluwarsa yang tidak lagi menerima pembaruan harus diganti.
                """
            )
    with right_column:
        image = Image.open("./images/prevention.jpg")
        st.image(image)
        st.write("[Learn More >](https://www.ocsia.im/advice-guidance/5-steps-to-cyber-security/)")

st.write("---")

st.video("https://www.youtube.com/watch?v=HWJJTO5mOaw&t=5s")

st.write("---")

with st.container():
    left_column, right_column = st.columns(2)
    with left_column:
        logo_patrolisiber = Image.open("./images/logo_patrolisiber.png")
        st.image(logo_patrolisiber, width=100)
        st.write("[Learn More >](https://www.patrolisiber.id/)")
    with right_column:
        logo_bssn = Image.open("./images/logo_bssn.png")
        st.image(logo_bssn, width=300)
        st.write("[Learn More >](https://bssn.go.id/)")

# ---- HIDE STREAMLIT STYLE ----
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)