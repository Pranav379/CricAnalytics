import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from data.utils import load_hawkeye_data
from batting.wagon_wheel import wagon_wheel
import altair as alt
st.title("Batter Hub")

# loading data
ipl_data = load_hawkeye_data()

# Fetching seasons for input
seasons = (ipl_data['season'].unique()).tolist()
seasons.sort()

# Fetching venues and converting them to shorter names for display purposes
venues_full_names = (ipl_data['ground'].unique()).tolist()
venues_short_names = [i.split("-")[-1] for i in venues_full_names if not pd.isna(i)]
venue_dict = {i.split("-")[-1]: i for i in venues_full_names if not pd.isna(i)}

# Getting input for batter name, seasons, and venues to consider
batter = st.selectbox("Batter name:", ipl_data['bat'].unique(), index = None, placeholder = "Select a batter name", key = "batter_name")
year = st.multiselect("Seasons:", seasons, key = "year")

st.write("")
container = st.container()
all = st.checkbox("Select all venues")
 
if all:
    venues_selected = container.multiselect("Venues:", venues_short_names, venues_short_names)
    venues = "ALL"    

else:
    venues_selected = container.multiselect("Venues:", venues_short_names)
    venues = [venue_dict[i] for i in venues_selected]








wagon_wheel(batter, ipl_data,seasons,venues)
