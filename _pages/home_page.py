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
        align-items: flex-start;
        gap: 70px;
        max-width: 1800px;
        margin: auto;
        padding: 50px 5px 20px;
        position: relative;
        min-height: 800px;
    }}
    .left-image {{
        position: absolute;
        left: -10px;
        top: 50px;
        width: 480px;   /* slightly increased width */
        height: 750px;  /* drastically increased height */
    }}
    .left-image img {{
        width: 100%;
        height: 100%;
        object-fit: contain;
        border-radius: 8px;
    }}
    .right-image {{
        position: absolute;
        right: -10px;
        top: 50px;
        width: 480px;   /* slightly increased width */
        height: 750px;  /* drastically increased height */
    }}
    .right-image img {{
        width: 100%;
        height: 100%;
        object-fit: contain;
        border-radius: 8px;
    }}
    .middle-content {{
        flex: 1;
        max-width: 700px;
        margin: 0 auto;
        text-align: left;
        position: relative;
        z-index: 10;
        padding: 0 20px;
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
    /* Align trophy image left edge with text */
    .center-image-container {{
        max-width: 1800px;
        margin: 10px auto 0;
        padding: 0 20px;
        position: relative;
    }}
    .center-image {{
        height: 450px;  /* moved higher by reducing height slightly */
        width: 750px;   /* increased width to reach second R in Premier */
        object-fit: contain;
        margin-left: calc(50% - 375px); /* align left edge with G in Get */
        display: block;
    }}
    
    /* Responsive adjustments */
    @media (max-width: 1400px) {{
        .left-image, .right-image {{
            display: none;
        }}
        .container {{
            padding: 20px;
        }}
        .center-image {{
            margin-left: 0;
            margin: 0 auto;
        }}
        .center-image-container {{
            text-align: center;
        }}
    }}
    </style>
    <div class="container">
        <div class="left-image">
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
        <div class="right-image">
            <img src="data:image/jpeg;base64,{encoded_right}" />
        </div>
    </div>
    <div class="center-image-container">
        <img src="data:image/jpeg;base64,{encoded_center}" class="center-image" />
    </div>
    """,
    unsafe_allow_html=True,
)