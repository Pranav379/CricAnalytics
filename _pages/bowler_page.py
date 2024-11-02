import streamlit as st



import matplotlib.pyplot as plt
from data.utils import load_hawkeye_data


st.title("Bowler Hub")





df=load_hawkeye_data()
df = df[["release_x", "release_y","release_z", "bowl","out","batruns", "bowl_style", "stump_y", "stump_z", "crease_z","crease_y","impact_z","impact_y","bounce_y"]]
df['bounce_z']=0




# Example DataFrame with bowlers' names and release points


# Define function for plotting release points of selected bowler
def plot_release_points(dataframe):
    # Dropdown menu to select a bowler
    selected_bowler = st.selectbox("Select a Bowler", dataframe['bowl'].unique())


    selected_location = st.selectbox("Choose an location:", ("Stump", "Release","Crease","Bounce","Impact"))
    # Filter data for the selected bowler
    bowler_data = dataframe[dataframe['bowl'] == selected_bowler]

    selected_bowl_type = bowler_data['bowl_style'].unique()
    st.write("Selected bowler uses "+selected_bowl_type[0]+" bowling style.")
    dismissed = bowler_data[bowler_data['out'] == True]
    not_dismissed_high_runs = bowler_data[(bowler_data['out'] == False) & (bowler_data['batruns']>3)]
    not_dismissed_low_runs=bowler_data[(bowler_data['out']== False) & (bowler_data['batruns']<4)]
    
    fig, ax = plt.subplots()


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
    
    ax.set_xlabel("Release Y")
    ax.set_ylabel("Release Z")
    ax.set_title(f"{selected_location} Points for {selected_bowler}")
    ax.legend()
    
    # Display the plot in Streamlit
    st.pyplot(fig)


def plot_pitcher_game_progression(dataframe):
    # Dropdown menu to select a bowler
    selected_bowler = st.selectbox("Select a Bowler", dataframe['bowl'].unique())


    selected_location = st.selectbox("Choose an location:", ("Stump", "Release","Crease","Bounce","Impact"))
    # Filter data for the selected bowler
    bowler_data = dataframe[dataframe['bowl'] == selected_bowler]

    selected_bowl_type = bowler_data['bowl_style'].unique()
    st.write("Selected bowler uses "+selected_bowl_type[0]+" bowling style.")
    dismissed = bowler_data[bowler_data['out'] == True]
    not_dismissed_high_runs = bowler_data[(bowler_data['out'] == False) & (bowler_data['batruns']>3)]
    not_dismissed_low_runs=bowler_data[(bowler_data['out']== False) & (bowler_data['batruns']<4)]
    
    fig, ax = plt.subplots()


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
    
    ax.set_xlabel("Release Y")
    ax.set_ylabel("Release Z")
    ax.set_title(f"{selected_location} Points for {selected_bowler}")
    ax.legend()
    
    # Display the plot in Streamlit
    st.pyplot(fig)

# Streamlit app
st.title("Bowl Coordinates")

# Call the function
plot_release_points(df)

st.title("Game progression")

plot_pitcher_game_progression(df)


