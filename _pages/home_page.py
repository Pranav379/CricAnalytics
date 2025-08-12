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

# Custom HTML + CSS top section: left img, middle text + spinning ball, right img side by side
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
        gap: 50px;
        max-width: 1400px;  /* wider container for bigger side images */
        margin: auto;
        padding-top: 20px;
    }}
    .side-image {{
        flex: 1.5;  /* increase from 1 to 1.5 to give more width */
        max-width: 280px;  /* max width of side images */
        height: 300px;  /* height roughly matching text block */
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
        flex: 4;  /* middle content wider than before */
        max-width: 600px;
    }}
    .heading {{
        display: flex;
        align-items: center;
        gap: 12px;
        margin-bottom: 0;
        font-size: 2.5rem;
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
                Get ready for a chase!
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

# Centered trophy image below the top section (bigger size)
st.markdown(
    f"""
    <div style="text-align: center; margin-top: 40px;">
        <img src="data:image/jpeg;base64,{encoded_center}" style="width: 380px; height: auto;" />
    </div>
    """,
    unsafe_allow_html=True,
)
