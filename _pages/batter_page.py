import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from data.utils import load_hawkeye_data
from batting.wagon_wheel import getZones
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






def wagon_wheel(batter, ipl_data,seasons,venues):
    zones = [1,2,3,4,5,6,7,8] 
    values = getZones(batter, ipl_data,seasons, venues)  
    equal_angle = 45  
    source = pd.DataFrame({
        "Zones": zones, 
        "value": [equal_angle] * len(zones), 
        "shots": values,
        "angle": [i * equal_angle + equal_angle / 2 for i in range(len(zones))] 
    })

    chart = alt.Chart(source).mark_arc(innerRadius=50).encode(
        theta=alt.Theta(field="value", type="quantitative"),  
        color=alt.Color(field="Zones", type="nominal"),
        tooltip=["Zones", "shots"]  
    )
    

    text = alt.Chart(source).mark_text(size=12, color='black').encode(
        theta=alt.Theta(field="angle", type="quantitative"), 
        radius=alt.value(100), 
        text=alt.Text(field="shots", type="quantitative")  
    )
    

    final_chart = chart + text
    

    st.altair_chart(final_chart.properties(
        title="Cricket Wagon Wheel: Shot Distribution by Region"
    ))


wagon_wheel(batter, ipl_data,seasons,venues)
