import streamlit as st
import base64

st.set_page_config(
    page_title="IPL Hawkeye Dashboard",
    layout="wide",
)

def load_base64(image_path):
    with open(image_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

encoded_cricketball = load_base64("images/cricketball.png")  
encoded_center = load_base64("images/IPLtrophy.jpg")  
encoded_left = load_base64("images/teampic.jpg")  
encoded_right = load_base64("images/srhwin.jpg")  

st.markdown(
    f"""
    <style>
    @keyframes spin {{
      from {{ transform: rotate(0deg); }}
      to {{ transform: rotate(360deg); }}
    }}

    .container {{
        display: flex;
        justify-content: center;
        align-items: center;
        gap: 60px;
        max-width: 1500px;  /* wider container */
        margin: auto;
        padding-top: 20px;
    }}
    .side-image {{
        flex: 2;  /* increased flex for wider images */
        max-width: 350px;  /* bigger max width */
        height: 400px;  /* increased height */
        display: flex;
        justify-content: center;
        align-items: center;
    }}
    .side-image img {{
        max-height: 100%;
        width: auto;
        object-fit: contain;
    }}
    .middle-content {{
        flex: 4.5;  /* slightly wider middle content */
        max-width: 700px;
    }}
    .heading {{
        display: flex;
        align-items: center;
        gap: 12px;
        margin-bottom: 0;
        font-size: 2.5rem;
        font-weight: 600;
    }}
    .heading span {{
        display: inline-block;
    }}
    .spin {{
        height: 1.5em;
        animation: spin 0.75s linear infinite;
    }}
    </style>

    <div class="container">
        <div class="side-image">
            <img src="data:image/jpeg;base64,{encoded_left}" />
        </div>
        <div class="middle-content">
            <h1>IPL Hawkeye Dashboard</h1>
            <h2>Welcome to this interactive dashboard analyzing cricket players in the 2023 and 2024 Indian Premier League (IPL) Seasons!</h2>
            <h2>Click on "Batter Hub" and "Bowler Hub" on the sidebar to explore further</h2>
            <div class="heading">
                <span>Get ready for a chase!</span>
                <img src="data:image/png;base64,{encoded_cricketball}" class="spin" />
            </div>
        </div>
        <div class="side-image">
            <img src="data:image/jpeg;base64,{encoded_right}" />
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# Bigger center trophy image with explicit width and height
st.markdown(
    f"""
    <div style="text-align: center; margin-top: 40px;">
        <img src="data:image/jpeg;base64,{encoded_center}" style="width: 650px; height: 450px; object-fit: contain;" />
    </div>
    """,
    unsafe_allow_html=True,
)
