import streamlit as st
import base64

st.set_page_config(
    page_title="IPL Hawkeye Dashboard",
    layout="centered"
)

st.title("IPL Hawkeye Dashboard")
st.markdown("## Welcome to this interactive dashboard analyzing cricket players in the 2023 and 2024 Indian Premier League (IPL) Seasons!")
st.markdown('## Click on "Batter Hub" and "Bowler Hub" on the sidebar to explore further')

# Convert image to Base64
with open("images/cricketball.png", "rb") as f:
    img_bytes = f.read()
encoded_img = base64.b64encode(img_bytes).decode()

# Inline heading with cricket ball that scales with text
st.markdown(
    f"""
    <h1 style='display: flex; align-items: center; gap: 10px;'>
        Get ready for a chase!
        <img src='data:image/png;base64,{encoded_img}' style='height: 1em;'>
    </h1>
    """,
    unsafe_allow_html=True
)
