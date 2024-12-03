from matplotlib import patches
import matplotlib.pyplot as plt
import streamlit as st

def plot_impact_vs_runs(df, player_name, seasons=None, venues=None):
    player_data = df 
    
    player_data = player_data[player_data['bowl'].str.contains(player_name)]

    if seasons:
        player_data = player_data.loc[player_data['season'].isin(seasons)]

    if venues:
        player_data = player_data.loc[player_data['ground'].isin(venues)]

    player_data['impactdist']=player_data['impact_x']-player_data['stump_x']
    
    fig, ax=plt.subplots()
    ax.scatter(player_data['impactdist'], player_data['batruns'], color='red', alpha=0.6, label="Dismissal")
    ax.set_xlim(0, 5)
    ax.set_title("Impact vs Bat Runs")
    ax.set_xlabel("Impact")
    ax.set_ylabel("Bat Runs")
    st.pyplot(fig)


