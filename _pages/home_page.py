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
        margin: 0;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI",
                     Roboto, Helvetica, Arial, sans-serif;
        color: rgb(49, 51, 63);
    }}

    .wrapper {{
        height: 100vh;
        display: flex;
        justify-content: center;
        align-items: center;
    }}

    .content {{
        max-width: 900px;
        padding: 20px;
        text-align: left;
    }}

    .title {{
        font-size: 2.6rem;
        font-weight: 700;
        margin-bottom: 26px;
    }}

    .text {{
        font-size: 1.5rem;
        font-weight: 400;
        line-height: 1.65;
        margin-bottom: 18px;
    }}

    .spin {{
        height: 34px;
        animation: spin 0.75s linear infinite;
        vertical-align: middle;
        margin-left: 6px;
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
                Click on <em>Batter Hub</em> and <em>Bowler Hub</em>
                on the sidebar to explore further
            </div>

            <div class="text">
                Get ready for a chase!
                <img src="data:image/png;base64,{encoded_cricketball}" class="spin">
            </div>
        </div>
    </div>
    """,
    height=680,
)