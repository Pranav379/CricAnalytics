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

    /* Use CSS grid for main layout */
    .main-grid {{
        display: grid;
        grid-template-columns: 20vw 1fr 20vw;  /* wide left and right columns */
        grid-template-rows: auto auto;
        gap: 20px 40px;
        max-width: 1600px;
        margin: auto;
        padding-top: 20px;
        align-items: center;
    }}

    .left-image, .right-image {{
        width: 100%;
        height: auto;
        max-height: 80vh;  /* big height but limited to viewport */
        object-fit: contain;
        justify-self: stretch;
        align-self: center;
    }}

    .center-text {{
        grid-column: 2;
        grid-row: 1;
        text-align: center;
        max-width: 700px;
        justify-self: center;
    }}

    .heading {{
        display: flex;
        align-items: center;
        justify-content: center;
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

    /* Center image aligned exactly under "Get" */
    .center-image {{
        grid-column: 2;
        grid-row: 2;
        justify-self: start; /* align left */
        margin-left: 1.7rem;  /* tweak this to align with G in Get */
        height: 650px;  /* taller */
        width: auto;
        object-fit: contain;
    }}

    </style>

    <div class="main-grid">
        <img src="data:image/jpeg;base64,{encoded_left}" alt="Left Team" class="left-image" />
        <div class="center-text">
            <h1>IPL Hawkeye Dashboard</h1>
            <h2>Welcome to this interactive dashboard analyzing cricket players in the 2023 and 2024 Indian Premier League (IPL) Seasons!</h2>
            <h2>Click on "Batter Hub" and "Bowler Hub" on the sidebar to explore further</h2>
            <div class="heading">
                <span>Get ready for a chase!</span>
                <img src="data:image/png;base64,{encoded_cricketball}" class="spin" />
            </div>
        </div>
        <img src="data:image/jpeg;base64,{encoded_right}" alt="Right Team" class="right-image" />
        
        <img src="data:image/jpeg;base64,{encoded_center}" alt="Trophy" class="center-image" />
    </div>
    """,
    unsafe_allow_html=True,
)
