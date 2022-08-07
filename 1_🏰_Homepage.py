import streamlit as st # pip install streamlit
import json # pip install jsons
from streamlit_lottie import st_lottie # pip install streamlit-lottie

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

lottie_welcome = load_lottiefile("./lottiefiles/cyber_welcome.json")
lottie_flower = load_lottiefile("./lottiefiles/cyber_flower.json")
lottie_header = load_lottiefile("./lottiefiles/cyber_header.json")
lottie_body = load_lottiefile("./lottiefiles/cyber_body.json")

# ---- SIDEBAR ----
with st.sidebar:
    st_lottie(lottie_welcome, height=200, key="welcome")
    st_lottie(lottie_flower, height=200, key="flower")

# ---- HEADER SECTION ----
st.markdown("<h1 style='text-align: center; color: silver;'>CYBERSECURITY</h1>", unsafe_allow_html=True)
st.markdown("##")
with st.container():
    st_lottie(lottie_header, height=200, key="header")
    st.markdown("##")
    st.write(
        """
        Cybersecurity adalah kumpulan teknologi, proses, dan praktik yang terlibat dalam melindungi individu dan organisasi dari cyber crime.
        Hal ini dirancang untuk melindungi integritas jaringan, komputer, program, dan data dari serangan, kerusakan, atau akses yang tidak sah.
        """
    )
    st.write("[Learn More >](https://www.cisco.com/c/en/us/products/security/what-is-cybersecurity.html)")

# ---- BODY SECTION ----
with st.container():
    st.write("---")
    st.header("History of Cybersecurity")
    st.markdown("##")
    left_column, right_column = st.columns(2)
    with left_column:
        st.write(
            """
            Pengecekan cybersecurity dimulai pada tahun 1970-an ketika peneliti Bob Thomas membuat program komputer yang disebut Creeper, yang dapat bergerak melintasi jaringan ARPANET.
            Ray Tomlinson, inovator email, menulis program Reaper, yang mengejar dan menghapus Creepers.
            Reaper adalah contoh pertama yang memeriksa perangkat lunak antivirus malware dan program yang mereplikasi diri sendiri, yaitu Virus, karena membuat worm dan trojan komputer pertama.
            """
        )
        st.write("[Learn More >](https://www.geeksforgeeks.org/history-of-cyber-security/#:~:text=The%20Cybersecurity%20checking%20began%20in,which%20chased%20and%20deleted%20Creepers.)")
    with right_column:
        st_lottie(lottie_body, height=300, key="body")

with st.container():
    st.write("---")
    st.header("Five Principles of Cybersecurity")
    st.markdown("##")
    left_column, right_column = st.columns(2)
    with left_column:
        st.write(
            """
            Lima prinsip utama cybersecurity adalah:
            - Confidentiality : Seperangkat aturan yang membatasi akses atau membatasi jenis informasi tertentu.
            - Integrity : Jaminan bahwa informasi tersebut dapat dipercaya dan akurat.
            - Availability : Jaminan akses yang dapat diandalkan ke informasi oleh orang yang berwenang.
            - Accountability : Merupakan jaminan bahwa individu atau organisasi akan dievaluasi kinerja atau perilakunya terkait dengan sesuatu yang menjadi tanggung jawabnya.
            - Auditability : Audit keamanan adalah evaluasi sistematis keamanan sistem informasi perusahaan dengan mengukur seberapa baik kesesuaiannya dengan serangkaian kriteria yang ditetapkan.
            """
        )
        st.write("[Learn More >](https://medium.com/@joepindar/five-principles-of-cybersecurity-back-to-basics-a8d1f0399d65)")
    with right_column:
        st.video("https://www.youtube.com/watch?v=hl1z7YYlHHY")
        st.caption("FIVE PRINCIPLES OF CYBERSECURITY - Back to Basics")
        st.write("by: [A Spoonful of Joe](https://www.youtube.com/user/TheIGNet)")