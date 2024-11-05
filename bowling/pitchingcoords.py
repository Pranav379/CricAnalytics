from matplotlib import patches
import matplotlib.pyplot as plt
import streamlit as st












# Example DataFrame with bowlers' names and release points


# Define function for plotting release points of selected bowler
def plot_release_points(dataframe):
    selected_season = st.selectbox("Select a Year: ", dataframe['season'].unique())
    season_data=dataframe[dataframe['season']==selected_season]

    selected_bowler = st.selectbox("Select a Bowler", season_data['bowl'].unique())
    bowler_data=season_data[season_data['bowl']==selected_bowler]
    
    
    selected_batter_hand = st.selectbox("Select batter hand:", ("LHB", "RHB"))
    handed_data=bowler_data[bowler_data['bat_hand']==selected_batter_hand]

    selected_location = st.selectbox("Choose an location:", ("Stump", "Release","Crease","Bounce","Impact"))


    # Filter data for the selected bowler

    selected_bowl_type = handed_data['bowl_style'].unique()
    st.write("Selected bowler uses "+selected_bowl_type[0]+" bowling style.")
    dismissed = handed_data[handed_data['out'] == True]
    not_dismissed_high_runs = handed_data[(handed_data['out'] == False) & (handed_data['batruns']>3)]
    not_dismissed_low_runs=handed_data[(handed_data['out']== False) & (handed_data['batruns']<4)]
    
    fig, ax = plt.subplots()

    ax.grid(True, color='gray', linestyle='-', linewidth=0.5, zorder=0)

    if(selected_location == "Release"):
        ax.scatter(dismissed['release_y'], dismissed['release_z'], color='red', alpha=0.6, label="Dismissal")
        ax.scatter(not_dismissed_low_runs['release_y'], not_dismissed_low_runs['release_z'], color='blue', alpha=0.6, label="<3 runs")
        ax.scatter(not_dismissed_high_runs['release_y'], not_dismissed_high_runs['release_z'], color='orange', alpha=0.6, label=">3 runs")
    if(selected_location =="Stump"):
        ax.scatter(dismissed['stump_y'], dismissed['stump_z'], color='red', alpha=0.6, label="Dismissal")
        ax.scatter(not_dismissed_low_runs['stump_y'], not_dismissed_low_runs['stump_z'], color='blue', alpha=0.6, label="<3 runs")
        ax.scatter(not_dismissed_high_runs['stump_y'], not_dismissed_high_runs['stump_z'], color='orange', alpha=0.6, label=">3 runs")
    if(selected_location =="Crease"):
        ax.scatter(dismissed['crease_y'], dismissed['crease_z'], color='red', alpha=0.6, label="Dismissal")
        ax.scatter(not_dismissed_low_runs['crease_y'], not_dismissed_low_runs['crease_z'], color='blue', alpha=0.6, label="<3 runs")
        ax.scatter(not_dismissed_high_runs['crease_y'], not_dismissed_high_runs['crease_z'], color='orange', alpha=0.6, label=">3 runs")
    if(selected_location =="Impact"):
        ax.scatter(dismissed['impact_y'], dismissed['impact_z'], color='red', alpha=0.6, label="Dismissal")
        ax.scatter(not_dismissed_low_runs['impact_y'], not_dismissed_low_runs['impact_z'], color='blue', alpha=0.6, label="<3 runs")
        ax.scatter(not_dismissed_high_runs['impact_y'], not_dismissed_high_runs['impact_z'], color='orange', alpha=0.6, label=">3 runs")
    if(selected_location =="Bounce"):
        ax.scatter(dismissed['bounce_y'], dismissed['bounce_z'], color='red', alpha=0.6, label="Dismissal")
        ax.scatter(not_dismissed_low_runs['bounce_y'], not_dismissed_low_runs['bounce_z'], color='blue', alpha=0.6, label="<3 runs")
        ax.scatter(not_dismissed_high_runs['bounce_y'], not_dismissed_high_runs['bounce_z'], color='orange', alpha=0.6, label=">3 runs")
    
    ax.set_xlim(-2, 2)  # Adjust these limits based on your data range for `y` coordinates
    ax.set_ylim(0, 2.3)

    rect = patches.Rectangle((-0.1143, 0), 0.04572, 0.7112, linewidth=1, edgecolor='brown', facecolor='brown', zorder=0)
    rect2 = patches.Rectangle((-0.02286, 0), 0.04572, 0.7112, linewidth=1, edgecolor='brown', facecolor='brown', zorder=0)
    rect3 = patches.Rectangle((0.06858, 0), 0.04572, 0.7112, linewidth=1, edgecolor='brown', facecolor='brown', zorder=0)
    ax.add_patch(rect)
    ax.add_patch(rect2)
    ax.add_patch(rect3)
    ax.set_xlabel("Release Y")
    ax.set_ylabel("Release Z")
    ax.set_title(f"{selected_location} Points for {selected_bowler}")
    ax.legend()
    
    # Display the plot in Streamlit
    st.pyplot(fig)


