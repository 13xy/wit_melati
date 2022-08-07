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

local_css("./style/style.css")

# Lottie Files: https://lottiefiles.com/
# ---- LOAD ASSETS ----
def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

lottie_power = load_lottiefile("./lottiefiles/cyber_power.json")

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
        st_lottie(lottie_power, height=200, key="power")

st.markdown("<h1 style='text-align: center; color: gold;'>TIPS AND TRICKS</h1>", unsafe_allow_html=True)
st.markdown("##")
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
        st.write("[Learn More >](https://www.ocsia.im/advice-guidance/5-steps-to-cyber-security/)")
    with right_column:
        image = Image.open("./images/prevention.jpg")
        st.image(image, caption="Five Preventative Cyber Security Tips")
        st.write("by: [dataversity](https://www.dataversity.net/seven-preventative-cyber-security-tips-smes-should-take-today/)")

with st.container():
    st.write("---")
    st.header("Cyber Crime Complaint")
    st.markdown("##")
    left_column, right_column = st.columns(2)
    with left_column:
        st.video("https://www.youtube.com/watch?v=HWJJTO5mOaw&t=5s")
        st.caption("Penanganan Insiden Siber | BSSN")
        st.write("by: [Badan Siber dan Sandi Negara](https://www.youtube.com/channel/UC-sdNDpQOIZM0vBt6D8Hw8A)")
    with right_column:
        alur_aduan_siber = Image.open("./images/alur_aduan_siber.jpg")
        st.image(alur_aduan_siber, caption="Alur Aduan Insiden Siber", width=300)
        st.write("by: [bssn](https://bssn.go.id/aduan-siber/)")
    
    left_column, right_column = st.columns(2)
    with left_column:
        logo_bssn = Image.open("./images/logo_bssn.png")
        st.image(logo_bssn, width=300)
        st.write("[Learn More >](https://bssn.go.id/)")
    with right_column:
        logo_patrolisiber = Image.open("./images/logo_patrolisiber.png")
        st.image(logo_patrolisiber, width=100)
        st.write("[Learn More >](https://www.patrolisiber.id/)")

with st.container():
    st.write("---")
    st.header("References")
    st.markdown("##")
    st.subheader("Article:")
    st.write(
        """
        - https://bssn.go.id/aduan-siber/
        - https://medium.com/@joepindar/five-principles-of-cybersecurity-back-to-basics-a8d1f0399d65
        - https://www.cisco.com/c/en/us/products/security/common-cyberattacks.html#~how-cyber-attacks-work
        - https://www.cisco.com/c/en/us/products/security/what-is-cybersecurity.html
        - https://www.dataversity.net/seven-preventative-cyber-security-tips-smes-should-take-today/
        - https://www.geeksforgeeks.org/history-of-cyber-security/#:~:text=The%20Cybersecurity%20checking%20began%20in,which%20chased%20and%20deleted%20Creepers.
        - https://www.ocsia.im/advice-guidance/5-steps-to-cyber-security/
        - https://www.stealthlabs.com/blog/cyber-security-threats-all-you-need-to-know/
        - https://www.upguard.com/blog/cyber-threat
        """
    )
    st.subheader("Media:")
    st.write(
        """
        - https://bssn.go.id/wp-content/uploads/2021/10/alur-aduan-siber.jpg
        - https://dv-website.s3.amazonaws.com/uploads/2019/01/Dataversity2_1reasons.jpg
        - https://www.stealthlabs.com/wp-content/uploads/2020/12/types-of-cybersecurity-threats.jpg
        - https://www.youtube.com/watch?v=hl1z7YYlHHY
        - https://www.youtube.com/watch?v=HWJJTO5mOaw&t=5s
        """
    )

with st.container():
    st.write("---")
    st.header("Thank You")
    st.markdown("##")
    left_column, right_column = st.columns(2)
    with left_column:
        logo_wit_s = Image.open("./images/logo_wit_s.jpg")
        st.image(logo_wit_s, width=300)
        st.write("Women in Tech - S")
    with right_column:
        logo_wit_2022 = Image.open("./images/logo_wit_2022.jpg")
        st.image(logo_wit_2022, width=300)
        st.write("Women in Tech - Thematic Academy 2022")

    left_column, middle_column, right_column = st.columns(3)
    with left_column:
        logo_netacad = Image.open("./images/logo_netacad.png")
        st.image(logo_netacad, width=150)
        st.write("[Learn More >](https://www.netacad.com/)")
    with middle_column:
        logo_digitalent = Image.open("./images/logo_digitalent.png")
        st.image(logo_digitalent, width=50)
        st.write("[Learn More >](https://digitalent.kominfo.go.id/)")
    with right_column:
        logo_kominfo = Image.open("./images/logo_kominfo.png")
        st.image(logo_kominfo, width=300)
        st.write("[Learn More >](https://www.kominfo.go.id/)")