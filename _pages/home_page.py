import streamlit as st

st.set_page_config(
    page_title="IPL Hawkeye Dashboard",
    layout="centered"
)

st.title("IPL Hawkeye Dashboard")
st.markdown("## Welcome to this interactive dashboard analyzing cricket players in the 2023 and 2024 Indian Premier League (IPL) Seasons!")
st.markdown('## Click on "Batter Hub" and "Bowler Hub" on the sidebar to explore further')

# Create two columns for text and image
col1, col2 = st.columns([3, 2])  # Adjust ratio for spacing

with col1:
    st.markdown("# Get ready for a chase!")

with col2:
    st.image("images/cricketball.png")
