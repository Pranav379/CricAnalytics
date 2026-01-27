import streamlit as st
import base64
import streamlit.components.v1 as components

st.set_page_config(
    page_title="IPL Hawkeye Dashboard",
    layout="wide",
)

def load_base64(image_path):
    with open(image_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

encoded_cricketball = load_base64("images/cricketball.png")

components.html(
    f"""
    <style>
    @keyframes spin {{
        from {{ transform: rotate(0deg); }}
        to {{ transform: rotate(360deg); }}
    }}

    body {{
        font-family: sans-serif;
        margin: 0;
    }}

    .wrapper {{
        height: 100vh;
        display: flex;
        justify-content: center;
        align-items: center;
    }}

    .content {{
        max-width: 900px;
        text-align: center;
        padding: 20px;
    }}

    .title {{
        font-size: 2.8rem;
        font-weight: 700;
        margin-bottom: 30px;
    }}

    .text {{
        font-size: 1.3rem;
        margin-bottom: 25px;
        line-height: 1.6;
    }}

    .heading {{
        display: flex;
        justify-content: center;
        align-items: center;
        gap: 12px;
        font-size: 2rem;
        font-weight: 600;
        margin-top: 30px;
    }}

    .spin {{
        height: 36px;
        animation: spin 0.75s linear infinite;
    }}
    </style>

    <div class="wrapper">
        <div class="content">
            <div class="title">IPL Hawkeye Dashboard</div>

            <div class="text">
                Welcome to this interactive dashboard analyzing cricket players
                in the 2023 and 2024 Indian Premier League (IPL) Seasons!
            </div>

            <div class="text">
                Click on <strong>Batter Hub</strong> and <strong>Bowler Hub</strong>
                on the sidebar to explore further
            </div>

            <div class="heading">
                <span>Get ready for a chase!</span>
                <img src="data:image/png;base64,{encoded_cricketball}" class="spin">
            </div>
        </div>
    </div>
    """,
    height=700,
)