import streamlit as st
import pandas as pd

from data.utils import load_hawkeye_data
from batting import *
# import altair as alt

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


# year = st.multiselect("Seasons:", seasons, key = "year")

# st.write("")
# container = st.container()
# all = st.checkbox("Select all venues")
#  
# if all:
#     venues_selected = container.multiselect("Venues:", venues_short_names, venues_short_names)
#     venues = "ALL"    

# else:
#     venues_selected = container.multiselect("Venues:", venues_short_names)
#     venues = [venue_dict[i] for i in venues_selected]


YEARS = [2023,  2024]       # Change later to do 


left, right = st.columns([1, 1])

if batter:
    batter_agg_stats = player_agg_stats(ipl_data, batter)
    batter_ten_sr = calculate_10_ball_sr(ipl_data, batter, YEARS)


    runs = batter_agg_stats['Runs']
    balls = batter_agg_stats['Balls']
    dismissals = batter_agg_stats['Dismissals']
    dot_ball_percent = batter_agg_stats['Dot %']
    boundary_percent = batter_agg_stats['Boundary %']



    left.subheader("Aggregate Statistics")
    left.write(f'{runs} runs in {balls} balls at {runs/dismissals:.2f}/{100 * runs/balls:.2f}')
    left.write(f'Dot % : {dot_ball_percent:.2f} | Boundary % : {boundary_percent:.2f}')
    left.write(f'Ten ball SR: {batter_ten_sr["Average 10 Ball SR"]:.2f}')

    wheel = wagon_wheel(batter, ipl_data, YEARS, None)

    right.write("")
    right.write("")
    right.altair_chart(wheel.properties(
        title=f"Wagon Wheel for {batter}"
    ))

    TYPES = ["SLA", "RM", "LBG", "RF", "RFM", "LMF", "OB", "LWS", "LFM", "LM", "LB", "LF", "OB/LB", "RM/OB/LB"]     # CHANGE LATER

    matchups = []

    for bowling_type in TYPES:
        matchup = get_matchup_stats(ipl_data, batter, bowling_type)
        balls = matchup["Total Balls"]
        sr = matchup['Strike Rate']
        if balls:
            runs = round(balls * sr / 100)
        dismissals = matchup['Dismissals']

        matchups.append([bowling_type, runs, balls, dismissals, sr])

    matchup_stats = pd.DataFrame(matchups, columns = ["Bowling Type", "Runs", "Balls", "Dismissals", "SR"])

    left.subheader("Matchups")
    left.dataframe(matchup_stats, hide_index = True)










