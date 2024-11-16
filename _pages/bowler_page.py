import streamlit as st
from bowling.pitchingcoords import plot_release_points
from bowling.gameprogression import plot_pitcher_game_progression
from bowling.liftdip import plot_bowler_lift_dip
from data.utils import load_hawkeye_data
from bowling.impactvsruns import plot_impact_vs_runs


st.title("Bowling Hub")

# Example of using the cached result
df = load_hawkeye_data()

plot_release_points(df)
plot_impact_vs_runs(df)
#plot_pitcher_game_progression(df)
#plot_bowler_lift_dip(df)

