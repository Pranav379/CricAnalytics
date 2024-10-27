import streamlit as st
from st_pages import add_page_title, get_nav_from_toml

# get and set up navigation to multi page app 
nav = get_nav_from_toml()
pg = st.navigation(nav)

# add_page_title(pg)

pg.run()