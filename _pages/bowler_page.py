import streamlit as st
import pandas as pd
from bowling.pitchingcoords import plot_release_points
from bowling.gameprogression import plot_pitcher_game_progression
from bowling.liftdip import plot_bowler_lift_dip
from data.utils import load_hawkeye_data
from bowling.impactvsruns import plot_impact_vs_runs
from bowling.agg_stats import bowling_agg_stats

st.title("Bowling Hub")

# Load IPL data
ipl_data = load_hawkeye_data()

# Fetching seasons and venues
seasons = sorted(ipl_data['season'].unique().tolist())
venues_full_names = ipl_data['ground'].dropna().unique().tolist()
venues_short_names = [i.split("-")[-1] for i in venues_full_names]
venue_dict = {i.split("-")[-1]: i for i in venues_full_names}

# Input selection
bowler = st.selectbox("Bowler name:", ipl_data['bowl'].unique(), index=0, key="bowler_name")
years = st.multiselect("Seasons:", seasons, [2023, 2024], key="year")

# Venue selection
container = st.container()
all_venues = st.checkbox("Select all venues")

if all_venues:
    venues_selected = container.multiselect("Venues:", venues_short_names, venues_short_names)
else:
    venues_selected = container.multiselect("Venues:", venues_short_names)

venues = [venue_dict[i] for i in venues_selected]

# Check if venues are selected
if bowler:
    # Calculate aggregate statistics
    bowler_agg_stats = bowling_agg_stats(ipl_data, bowler, years, venues)

    # Check if the bowler has played in selected venues
    if bowler_agg_stats['Games'] == 0:
        st.warning(f"No data available for {bowler} in the selected venues. "
                   f"It seems they haven't played any games in these venues.")
    else:
        # Display aggregate statistics
        st.subheader("Aggregate Statistics")
        
        games = bowler_agg_stats['Games']
        overs = bowler_agg_stats['Overs']
        economy = bowler_agg_stats['Economy']
        power_percentage = bowler_agg_stats['Power_Percentage']
        power_control = bowler_agg_stats['Power_Control']
        player_deviation = bowler_agg_stats['Player_Deviation']
        average_deviation = bowler_agg_stats['Average_Deviation']
        deviation_comparison = bowler_agg_stats['Deviation_Comparison']
        middle_percentage = bowler_agg_stats['Middle_Percentage']
        middle_control = bowler_agg_stats['Middle_Control']
        death_percentage = bowler_agg_stats['Death_Percentage']
        death_control = bowler_agg_stats['Death_Control']

        st.write(
            f'Games: {games} | Overs: {overs:.1f} | Economy: {economy:.2f}'
        )

        st.write(
            f'Powerplay %: {power_percentage*100:.2f} | Powerplay Control: {power_control:.2f}| Player Deviation: {player_deviation:.2f} | All Player\'s Average Deviation: {average_deviation:.2f}'
        )

        st.write(
            f'Middle Overs %: {middle_percentage*100:.2f}| Middle Overs Control: {middle_control:.2f}| Death Overs %: {death_percentage*100:.2f} | Death Overs Control: {death_control:.2f}'
        )

    
    st.subheader("Release Points")
    plot_release_points(ipl_data,bowler, years, venues)

    st.subheader("Game Progression")
    plot_pitcher_game_progression(ipl_data, bowler, years, venues)

    st.subheader("Bowler Lift")
    plot_bowler_lift_dip(ipl_data,bowler, years, venues)

    st.subheader("Impact vs Bat Runs")
    plot_impact_vs_runs(ipl_data,bowler, years, venues)
