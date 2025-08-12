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
        gap: 70px;
        max-width: 1600px;
        margin: auto;
        padding-top: 20px;
    }}
    .side-image {{
        flex: 3;  /* much bigger flex */
        max-width: 600px;  /* drastically increased max width */
        height: 700px;  /* drastically increased height */
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
        flex: 4.5;
        max-width: 700px;
        position: relative;
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

    /* Align center image left edge with 'G' in "Get" */
    .center-image-container {{
        max-width: 700px;
        margin-top: 40px;
        position: relative;
    }}
    .center-image {{
        height: 600px;  /* increase height more */
        width: 520px;   /* width less than height */
        object-fit: contain;
        margin-left: 54px; /* tweak this margin to align left edge with G */
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

    <div class="center-image-container">
        <img src="data:image/jpeg;base64,{encoded_center}" class="center-image" />
    </div>
    """,
    unsafe_allow_html=True,
)
