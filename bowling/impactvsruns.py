from matplotlib import patches
import matplotlib.pyplot as plt
import streamlit as st

def plot_impact_vs_runs(dataframe):
    selected_season = st.selectbox("Select a Year: ", dataframe['season'].unique(), key="howdy")
    season_data=dataframe[dataframe['season']==selected_season]

    selected_bowler = st.selectbox("Select a Bowler", season_data['bowl'].unique(), key="howdy1")
    bowler_data=season_data[season_data['bowl']==selected_bowler]
    
    
    selected_batter_hand = st.selectbox("Select batter hand:", ("LHB", "RHB"), key="howdy2")
    handed_data=bowler_data[bowler_data['bat_hand']==selected_batter_hand]

    handed_data['impactdist']=handed_data['impact_x']-handed_data['stump_x']
    
    fig, ax=plt.subplots()
    ax.scatter(handed_data['impactdist'], handed_data['batruns'], color='red', alpha=0.6, label="Dismissal")
    ax.set_xlim(0, 5)
    st.pyplot(fig)


