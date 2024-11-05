import streamlit as st
from bowling.pitchingcoords import plot_release_points
from data.utils import load_hawkeye_data


st.title("Batter Hub")

# Example of using the cached result
df = load_hawkeye_data()
df.iloc[:4, :20]

plot_release_points(df)

