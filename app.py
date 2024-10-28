import streamlit as st
from st_pages import add_page_title, get_nav_from_toml
from data.utils import load_hawkeye_data

# get and set up navigation to multi page app 
nav = get_nav_from_toml()
pg = st.navigation(nav)
pg.run()

hawkeye_df = load_hawkeye_data()

