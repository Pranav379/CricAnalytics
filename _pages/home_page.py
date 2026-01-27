import streamlit as st
import base64

st.set_page_config(
    page_title="IPL Hawkeye Dashboard",
    layout="wide",
)

def load_base64(image_path):
    with open(image_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

# Load ONLY the cricket ball
encoded_cricketball = load_base64("images/cricketball.png")

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
        max-width: 1200px;
        margin: auto;
        padding: 50px 20px;
        min-height: 80vh;
    }}

    .middle-content {{
        max-width: 800px;
        text-align: left;
    }}

    .heading {{
        display: flex;
        align-items: center;
        gap: 12px;
        margin-top: 20px;
        font-size: 2.5rem;
        font-weight: 600;
    }}

    .spin {{
        height: 1.5em;
        animation: spin 0.75s linear infinite;
    }}
    </style>

    <div class="container">
        <div class="middle-content">
            <h1>IPL Hawkeye Dashboard</h1>

            <h2>
                Welcome to this interactive dashboard analyzing cricket players
                in the 2023 and 2024 Indian Premier League (IPL) Seasons!
            </h2>

            <h2>
                Click on "Batter Hub" and "Bowler Hub" on the sidebar to explore further
            </h2>

            <div class="heading">
                <span>Get ready for a chase!</span>
                <img src="data:image/png;base64,{encoded_cricketball}" class="spin" />
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)
