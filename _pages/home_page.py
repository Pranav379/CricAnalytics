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

# Inline heading with spinning cricket ball, sized bigger (~1.5em)
st.markdown(
    f"""
    <style>
    @keyframes spin {{
      from {{ transform: rotate(0deg); }}
      to {{ transform: rotate(360deg); }}
    }}
    .spin {{
      animation: spin 4s linear infinite;
      height: 1.5em;
    }}
    </style>
    <h1 style='display: flex; align-items: center; gap: 12px;'>
        Get ready for a chase!
        <img src='data:image/png;base64,{encoded_img}' class='spin'>
    </h1>
    """,
    unsafe_allow_html=True
)
