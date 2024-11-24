import streamlit as st
import pandas as pd

from data.utils import load_hawkeye_data
from batting import *

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
batter = st.selectbox("Batter name:", ipl_data['bat'].unique(), index = 0, key = "batter_name")


years = st.multiselect("Seasons:", seasons, [2023, 2024], key = "year")

container = st.container()
all = st.checkbox("Select all venues")
 
if all:
    venues_selected = container.multiselect("Venues:", venues_short_names, venues_short_names)
    venues = [venue_dict[i] for i in venues_selected]  

else:
    venues_selected = container.multiselect("Venues:", venues_short_names)
    venues = [venue_dict[i] for i in venues_selected]




if batter:
    batter_agg_stats = player_agg_stats(ipl_data, batter, years, venues)
    batter_ten_sr = calculate_10_ball_sr(ipl_data, batter, years, venues)


    runs = batter_agg_stats['Runs']
    balls = batter_agg_stats['Balls']
    dismissals = batter_agg_stats['Dismissals']
    dot_ball_percent = batter_agg_stats['Dot %']
    boundary_percent = batter_agg_stats['Boundary %']
    innings = batter_agg_stats['Innings']

    st.subheader("Aggregate Statistics")
    st.write(f'Innings: {innings} | Runs: {runs} | Balls: {balls} | Average {runs/dismissals:.2f} | Strike Rate: {100 * runs/balls:.2f} | Dot % : {dot_ball_percent:.2f} | Boundary % : {boundary_percent:.2f}')
    st.write(f'Ten ball SR: {batter_ten_sr["Average 10 Ball SR"]:.2f}')


    left, right = st.columns([1, 1])

    wheel = wagon_wheel(batter, ipl_data, years, venues)

    right.write("")
    right.write("")
    right.altair_chart(wheel.properties(
        title=f"Wagon Wheel for {batter}"
    ))

    TYPES = ["SLA", "RM", "LBG", "RF", "RFM", "LMF", "OB", "LWS", "LFM", "LM", "LB", "LF"] 

    matchups = []

    for bowling_type in TYPES:
        matchup = get_matchup_stats(ipl_data, batter, bowling_type, venues, years)
        balls = matchup["Total Balls"]
        sr = matchup['Strike Rate']
        if balls:
            runs = round(balls * sr / 100)
        dismissals = matchup['Dismissals']

        matchups.append([bowling_type, runs, balls, dismissals, sr])

    matchup_stats = pd.DataFrame(matchups, columns = ["Type", "Runs", "Balls", "Outs", "SR"])

    left.subheader("Matchups")
    left.dataframe(matchup_stats, hide_index = True)










