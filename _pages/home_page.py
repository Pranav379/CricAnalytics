import streamlit as st

st.set_page_config(
    page_title="IPL Hawkeye Dashboard",
    layout="centered"
)

st.title("IPL Hawkeye Dashboard")
st.markdown("## Welcome to this interactive dashboard analyzing cricket players in the 2023 and 2024 Indian Premier League (IPL) Seasons!")
st.markdown('## Click on "Batter Hub" and "Bowler Hub" on the sidebar to explore further')

# Inline heading with cricket ball image that scales with text
st.markdown(
    """
    <h1 style='display: flex; align-items: center; gap: 10px;'>
        Get ready for a chase!
        <img src='https://github.com/Pranav379/CricAnalytics/blob/main/images/cricketball.png' style='height: 1em;'>
    </h1>
    """,
    unsafe_allow_html=True
)