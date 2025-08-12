import streamlit as st
import base64

st.set_page_config(
    page_title="IPL Hawkeye Dashboard",
    layout="wide"  # Use wide layout for full horizontal space
)

def load_base64(image_path):
    with open(image_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

encoded_cricketball = load_base64("../images/cricketball.png")      # PNG for spinning ball
encoded_center = load_base64("../images/center_image.jpg")          # JPG for center image
encoded_left = load_base64("../images/left_image.jpg")              # JPG for left image
encoded_right = load_base64("../images/right_image.jpg")            # JPG for right image

# Create three columns: left, middle, right
col_left, col_mid, col_right = st.columns([1, 3, 1])

with col_left:
    st.markdown(
        f"""
        <div style="
            height: 90vh;  /* Nearly full viewport height */
            display: flex;
            justify-content: center;
            align-items: center;
            ">
            <img 
                src="data:image/jpeg;base64,{encoded_left}" 
                style="
                    max-height: 90vh; 
                    width: auto; 
                    max-width: 100%; 
                    object-fit: contain;
                ">
        </div>
        """,
        unsafe_allow_html=True,
    )

with col_mid:
    st.markdown("# IPL Hawkeye Dashboard")
    st.markdown(
        "## Welcome to this interactive dashboard analyzing cricket players in the 2023 and 2024 Indian Premier League (IPL) Seasons!"
    )
    st.markdown('## Click on "Batter Hub" and "Bowler Hub" on the sidebar to explore further')

    # Inline heading with spinning cricket ball
    st.markdown(
        f"""
        <h1 style='display: flex; align-items: center; gap: 12px; margin-bottom: 0;'>
            Get ready for a chase!
            <img src='data:image/png;base64,{encoded_cricketball}' style='height: 1.5em; animation: spin 0.75s linear infinite;'>
        </h1>

        <style>
        @keyframes spin {{
          from {{ transform: rotate(0deg); }}
          to {{ transform: rotate(360deg); }}
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )

with col_right:
    st.markdown(
        f"""
        <div style="
            height: 90vh;
            display: flex;
            justify-content: center;
            align-items: center;
            ">
            <img 
                src="data:image/jpeg;base64,{encoded_right}" 
                style="
                    max-height: 90vh; 
                    width: auto; 
                    max-width: 100%; 
                    object-fit: contain;
                ">
        </div>
        """,
        unsafe_allow_html=True,
    )

# Centered image below the top section
st.markdown(
    f"""
    <div style="text-align: center; margin-top: 20px;">
        <img src="data:image/jpeg;base64,{encoded_center}" style="max-width: 200px;">
    </div>
    """,
    unsafe_allow_html=True,
)
