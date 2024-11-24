import matplotlib.pyplot as plt
import streamlit as st

def plot_bowler_lift_dip(df, player_name, seasons=None, venues=None):
    player_data = df 
    
    player_data = player_data[player_data['bowl'].str.contains(player_name)]

    if seasons:
        player_data = player_data.loc[player_data['season'].isin(seasons)]

    if venues:
        player_data = player_data.loc[player_data['ground'].isin(venues)]

    # Calculate lift/dip by comparing post_bounce_ay with gravity
    gravity = 9.8
    player_data['lift_dip'] = player_data['pre_bounce_az'] + gravity

    x_axis_options = ['release_speed', 'cur_bowl_ovr', 'initial_angle', 'drop_angle','swing','devation','batruns']
    selected_x_axis = st.selectbox("Select X-Axis", x_axis_options)

    # Filter out rows where lift/dip is greater than ±15
    player_data = player_data[(player_data['lift_dip'] <= 15) & (player_data['lift_dip'] >= -15)]

    # Separate dismissed, 4s, 6s, and other deliveries for color differentiation
    dismissed = player_data[player_data['out'] == True]
    fours = player_data[player_data['batruns'] == 4]
    sixes = player_data[player_data['batruns'] == 6]
    not_dismissed = player_data[(player_data['out'] == False) & (player_data['batruns'] < 4)]

    # Plot lift/dip with the chosen x-axis variable
    fig, ax = plt.subplots()

    # Plot deliveries with different markers/colors
    ax.scatter(not_dismissed[selected_x_axis], not_dismissed['lift_dip'], color='blue', alpha=0.6, label="No Dismissal (<4 runs)")
    ax.scatter(fours[selected_x_axis], fours['lift_dip'], color='green', alpha=0.6, label="4s")
    ax.scatter(sixes[selected_x_axis], sixes['lift_dip'], color='purple', alpha=0.6, label="6s")
    ax.scatter(dismissed[selected_x_axis], dismissed['lift_dip'], color='red', alpha=0.6, label="Dismissal")

    # Set labels and title
    ax.set_xlabel(selected_x_axis.replace('_', ' ').title())
    ax.set_ylabel("Lift/Dip (m/s²)")
    ax.set_title(f"Lift/Dip vs. {selected_x_axis.replace('_', ' ').title()} for {player_name} in {', '.join(map(str, seasons))}")
    ax.legend()

    # Display the plot in Streamlit
    st.pyplot(fig)