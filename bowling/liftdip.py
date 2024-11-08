import matplotlib.pyplot as plt
import streamlit as st

def plot_bowler_lift_dip(dataframe):
    # Dropdown to select a bowler
    selected_bowler = st.selectbox("Select a Bowler", dataframe['bowl'].unique())
    
    # Dropdown to select a year
    selected_year = st.selectbox("Select a Year", sorted(dataframe['season'].unique()))
    
    # Dropdown to select the x-axis variable
    x_axis_options = ['release_speed', 'cur_bowl_ovr', 'initial_angle', 'drop_angle','swing','devation','batruns']
    selected_x_axis = st.selectbox("Select X-Axis", x_axis_options)
    
    # Filter data for the selected bowler and year
    bowler_data = dataframe[(dataframe['bowl'] == selected_bowler) & (dataframe['season'] == selected_year)]

    # Calculate lift/dip by comparing post_bounce_ay with gravity
    gravity = 9.8
    bowler_data['lift_dip'] = bowler_data['pre_bounce_az'] + gravity

    # Filter out rows where lift/dip is greater than ±15
    bowler_data = bowler_data[(bowler_data['lift_dip'] <= 15) & (bowler_data['lift_dip'] >= -15)]

    # Separate dismissed, 4s, 6s, and other deliveries for color differentiation
    dismissed = bowler_data[bowler_data['out'] == True]
    fours = bowler_data[bowler_data['batruns'] == 4]
    sixes = bowler_data[bowler_data['batruns'] == 6]
    not_dismissed = bowler_data[(bowler_data['out'] == False) & (bowler_data['batruns'] < 4)]

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
    ax.set_title(f"Lift/Dip vs. {selected_x_axis.replace('_', ' ').title()} for {selected_bowler} in {selected_year}")
    ax.legend()

    # Display the plot in Streamlit
    st.pyplot(fig)