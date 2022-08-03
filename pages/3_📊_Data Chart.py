import streamlit as st
import pandas as pd
import plotly.express as px
import base64
from io import StringIO, BytesIO

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

# ---- DOWNLOAD LINK ----
# Credit Excel: https://discuss.streamlit.io/t/how-to-add-a-download-excel-csv-function-to-a-button/4474/5
def generate_excel_download_link(df):
    towrite = BytesIO()
    df.to_excel(towrite, encoding="utf-8", index=False, header=True)  # write to BytesIO buffer
    towrite.seek(0)  # reset pointer
    b64 = base64.b64encode(towrite.read()).decode()
    href = f'<a href="data:application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;base64,{b64}" download="data_table.xlsx">Download Excel File</a>'
    return st.markdown(href, unsafe_allow_html=True)

# Credit Plotly: https://discuss.streamlit.io/t/download-plotly-plot-as-html/4426/2
def generate_html_download_link(fig):
    towrite = StringIO()
    fig.write_html(towrite, include_plotlyjs="cdn")
    towrite = BytesIO(towrite.getvalue().encode())
    b64 = base64.b64encode(towrite.read()).decode()
    href = f'<a href="data:text/html;charset=utf-8;base64, {b64}" download="chart.html">Download Chart</a>'
    return st.markdown(href, unsafe_allow_html=True)

# ---- READ EXCEL ----
df = pd.read_excel(
    io="./data/data_threats.xlsx",
    engine="openpyxl",
    sheet_name="Data",
    skiprows=3,
    usecols="B:E",
    nrows=103,
)

# ---- SIDEBAR ----
st.sidebar.header("Silakan pilih :")
tahun = st.sidebar.selectbox(
    "Pilih tahun :",
    options=df["Tahun"].unique()
)

bulan = st.sidebar.multiselect(
    "Pilih bulan :",
    options=df["Bulan"].unique(),
    default=df["Bulan"].unique()
)

threats = st.sidebar.multiselect(
    "Pilih threats :",
    options=df["Threats"].unique(),
    default=df["Threats"].unique()
)

df_selection = df.query(
    "Tahun == @tahun & Bulan == @bulan & Threats == @threats"
)

# Icons: https://icons.getbootstrap.com/
# ---- MAINPAGE ----
st.title(":bar_chart: Threats Dashboard")
st.markdown("##")

# ---- TOP TOTAL ----
jumlah = int(df_selection["Jumlah"].sum())

with st.container():
    st.write("---")
    left_column, middle_column, right_column = st.columns(3)
    with left_column:
        st.subheader("Tahun : ")
        st.subheader(tahun)
    with middle_column:
        st.subheader("Bulan : ")
        st.caption(bulan)
    with right_column:
        st.subheader("Threats : ")
        st.caption(threats)

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.subheader("Total Anomali Trafik :")
    with right_column:
        st.subheader(f"{jumlah:,}")

# ---- DATAFRAME ----
with st.container():
    st.write("---")
    if st.checkbox("Tampilkan dataframe"):
        st.dataframe(df_selection)
    generate_excel_download_link(df_selection)

# ---- TOTAL BY THREATS [BAR CHART] ----
total_by_threats = (
    df_selection.groupby(by=["Threats"]).sum()[["Jumlah"]].sort_values(by="Jumlah")
)
fig_threats = px.bar(
    total_by_threats,
    x="Jumlah",
    y=total_by_threats.index,
    orientation="h",
    title="<b>Total by Threats</b>",
    color_discrete_sequence=["#0083B8"] * len(total_by_threats),
    template="plotly_white",
)
fig_threats.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False))
)

# ---- TOTAL BY TAHUN BULAN [BAR CHART] ----
total_by_tahun_bulan = (
    df_selection.groupby(by=["Bulan"]).sum()[["Jumlah"]].sort_values(by="Jumlah")
)
fig_tahun_bulan = px.bar(
    total_by_tahun_bulan,
    x=total_by_tahun_bulan.index,
    y="Jumlah",
    title="<b>Total by Tahun and Bulan</b>",
    color_discrete_sequence=["#0083B8"] * len(total_by_tahun_bulan),
    template="plotly_white",  
)
fig_tahun_bulan.update_layout(
    xaxis=dict(tickmode="linear"),
    plot_bgcolor="rgba(0,0,0,0)",
    yaxis=(dict(showgrid=False)),
)

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.plotly_chart(fig_threats, use_container_width=True)
        generate_html_download_link(fig_threats)
    with right_column:
        st.plotly_chart(fig_tahun_bulan, use_container_width=True)
        generate_html_download_link(fig_tahun_bulan)