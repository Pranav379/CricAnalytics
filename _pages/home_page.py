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

    .ball-container {{
        display: flex;
        justify-content: center;
        align-items: center;
        height: 80vh;
    }}

    .spin {{
        height: 120px;
        animation: spin 0.75s linear infinite;
    }}
    </style>

    <div class="ball-container">
        <img src="data:image/png;base64,{encoded_cricketball}" class="spin" />
    </div>
    """,
    unsafe_allow_html=True,
)