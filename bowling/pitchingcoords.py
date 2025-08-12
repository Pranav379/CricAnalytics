from matplotlib import patches
import matplotlib.pyplot as plt
import streamlit as st


# Define function for plotting release points of selected bowler
def plot_release_points(df, player_name, seasons=None, venues=None):

    player_data= df[df['bowl'].str.contains(player_name)]

    if seasons:
        player_data = player_data.loc[player_data['season'].isin(seasons)]

    if venues:
        player_data = player_data.loc[player_data['ground'].isin(venues)]
    
    selected_batter_hand = st.selectbox("Select batter hand:", ("LHB", "RHB"), key='batter_hand')
    player_data = player_data[player_data['bat_hand'] == selected_batter_hand]
    player_data['bounce_z']=0

    selected_location = st.selectbox("Choose a location:", ("Stump", "Release","Crease","Bounce","Impact"),key="location")


    # Filter data for the selected bowler

    selected_bowl_type = player_data['bowl_style'].unique()
    st.write("Selected bowler uses "+selected_bowl_type[0]+" bowling style.")
    dismissed = player_data[player_data['out'] == True]
    not_dismissed_high_runs = player_data[(player_data['out'] == False) & (player_data['batruns']>3)]
    not_dismissed_low_runs=player_data[(player_data['out']== False) & (player_data['batruns']<4)]
    
    # fig, ax = plt.subplots()
    fig, (ax, ax1) = plt.subplots(1, 2, figsize=(12, 6), gridspec_kw={'width_ratios': [2, 1]})

    ax.grid(True, color='gray', linestyle='-', linewidth=0.5, zorder=0)

    if(selected_location == "Release"):
        ax.scatter(dismissed['release_y'], dismissed['release_z'], color='red', alpha=0.6, label="Dismissal")
        ax.scatter(not_dismissed_low_runs['release_y'], not_dismissed_low_runs['release_z'], color='blue', alpha=0.6, label="<=3 runs")
        ax.scatter(not_dismissed_high_runs['release_y'], not_dismissed_high_runs['release_z'], color='orange', alpha=0.6, label=">3 runs")
    if(selected_location =="Stump"):
        ax.scatter(dismissed['stump_y'], dismissed['stump_z'], color='red', alpha=0.6, label="Dismissal")
        ax.scatter(not_dismissed_low_runs['stump_y'], not_dismissed_low_runs['stump_z'], color='blue', alpha=0.6, label="<=3 runs")
        ax.scatter(not_dismissed_high_runs['stump_y'], not_dismissed_high_runs['stump_z'], color='orange', alpha=0.6, label=">3 runs")
    if(selected_location =="Crease"):
        ax.scatter(dismissed['crease_y'], dismissed['crease_z'], color='red', alpha=0.6, label="Dismissal")
        ax.scatter(not_dismissed_low_runs['crease_y'], not_dismissed_low_runs['crease_z'], color='blue', alpha=0.6, label="<=3 runs")
        ax.scatter(not_dismissed_high_runs['crease_y'], not_dismissed_high_runs['crease_z'], color='orange', alpha=0.6, label=">3 runs")
    if(selected_location =="Impact"):
        ax.scatter(dismissed['impact_y'], dismissed['impact_z'], color='red', alpha=0.6, label="Dismissal")
        ax.scatter(not_dismissed_low_runs['impact_y'], not_dismissed_low_runs['impact_z'], color='blue', alpha=0.6, label="<=3 runs")
        ax.scatter(not_dismissed_high_runs['impact_y'], not_dismissed_high_runs['impact_z'], color='orange', alpha=0.6, label=">3 runs")
    if(selected_location =="Bounce"):
        ax.scatter(dismissed['bounce_y'], dismissed['bounce_z'], color='red', alpha=0.6, label="Dismissal")
        ax.scatter(not_dismissed_low_runs['bounce_y'], not_dismissed_low_runs['bounce_z'], color='blue', alpha=0.6, label="<=3 runs")
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
    ax.set_title(f"{selected_location} Points for {player_name}")
    ax.legend()
    
    # Display the plot in Streamlit
    


    # fig1, ax1 = plt.subplots()

    ax1.grid(True, color='gray', linestyle='-', linewidth=0.5, zorder=0)

    ax1.set_xlim(-2, 2)  # Adjust these limits based on your data range for `y` coordinates
    ax1.set_ylim(-15, 15)

    if(selected_location == "Release"):
        ax1.scatter(dismissed['release_y'], dismissed['release_x'], color='red', alpha=0.6, label="Dismissal")
        ax1.scatter(not_dismissed_low_runs['release_y'], not_dismissed_low_runs['release_x'], color='blue', alpha=0.6, label="<=3 runs")
        ax1.scatter(not_dismissed_high_runs['release_y'], not_dismissed_high_runs['release_x'], color='orange', alpha=0.6, label=">3 runs")
    if(selected_location =="Stump"):
        ax1.scatter(dismissed['stump_y'], dismissed['stump_x'], color='red', alpha=0.6, label="Dismissal")
        ax1.scatter(not_dismissed_low_runs['stump_y'], not_dismissed_low_runs['stump_x'], color='blue', alpha=0.6, label="<=3 runs")
        ax1.scatter(not_dismissed_high_runs['stump_y'], not_dismissed_high_runs['stump_x'], color='orange', alpha=0.6, label=">3 runs")
    if(selected_location =="Crease"):
        ax1.scatter(dismissed['crease_y'], dismissed['crease_x'], color='red', alpha=0.6, label="Dismissal")
        ax1.scatter(not_dismissed_low_runs['crease_y'], not_dismissed_low_runs['crease_x'], color='blue', alpha=0.6, label="<=3 runs")
        ax1.scatter(not_dismissed_high_runs['crease_y'], not_dismissed_high_runs['crease_x'], color='orange', alpha=0.6, label=">3 runs")
    if(selected_location =="Impact"):
        ax1.scatter(dismissed['impact_y'], dismissed['impact_x'], color='red', alpha=0.6, label="Dismissal")
        ax1.scatter(not_dismissed_low_runs['impact_y'], not_dismissed_low_runs['impact_x'], color='blue', alpha=0.6, label="<=3 runs")
        ax1.scatter(not_dismissed_high_runs['impact_y'], not_dismissed_high_runs['impact_x'], color='orange', alpha=0.6, label=">3 runs")
        ax1.set_xlim(-2, 2)  # Adjust these limits based on your data range for `y` coordinates
        ax1.set_ylim(-15, -5)
    if(selected_location =="Bounce"):
        ax1.scatter(dismissed['bounce_y'], dismissed['bounce_x'], color='red', alpha=0.6, label="Dismissal")
        ax1.scatter(not_dismissed_low_runs['bounce_y'], not_dismissed_low_runs['bounce_x'], color='blue', alpha=0.6, label="<=3 runs")
        ax1.scatter(not_dismissed_high_runs['bounce_y'], not_dismissed_high_runs['bounce_x'], color='orange', alpha=0.6, label=">3 runs")
        ax1.set_xlim(-2, 2)  # Adjust these limits based on your data range for `y` coordinates
        ax1.set_ylim(-15, 30)
    
    

    rect = patches.Rectangle((-0.1143, -15), 0.04572, 100, linewidth=1, edgecolor='brown', facecolor='brown', zorder=0)
    rect2 = patches.Rectangle((-0.02286, -15), 0.04572, 100, linewidth=1, edgecolor='brown', facecolor='brown', zorder=0)
    rect3 = patches.Rectangle((0.06858, -15), 0.04572, 100, linewidth=1, edgecolor='brown', facecolor='brown', zorder=0)
    rect4 = patches.Rectangle((-2.5,-10.15), 5, 0.30, linewidth=1, edgecolor='grey', facecolor='grey', zorder=0)

    ax1.add_patch(rect)
    ax1.add_patch(rect2)
    ax1.add_patch(rect3)
    ax1.add_patch(rect4)
    ax1.set_xlabel("Release Y")
    ax1.set_ylabel("Release X")
    ax1.set_title(f"{selected_location} Points for {player_name}")
    ax1.legend()
    
    # Display the plot in Streamlit
    # st.pyplot(fig1)
    st.pyplot(fig)


