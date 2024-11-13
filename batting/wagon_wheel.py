import pandas as pd
import altair as alt
import streamlit as st

def getZones(playername, df, seasons=None, venues=None):
    print(playername)
    batter = df.loc[df['bat'] == playername]  

    if seasons:
        print(seasons)
        batter = batter[batter['season'].isin(seasons)]  
    print(venues)
    if venues:
        venue_pattern = '|'.join(venues)
        print(venue_pattern)
        batter = batter[batter['ground'].str.contains(venue_pattern, case=False, na=False)]
    
    print(batter) 
    zones = [0, 0, 0, 0, 0, 0, 0, 0]

    for row in batter.itertuples(index=True, name="Row"):
        zones[int(row.wagonZone) - 1] += 1

    return zones


def wagon_wheel(batter, ipl_data,seasons,venues):
    zones = [1,2,3,4,5,6,7,8] 
    values = getZones(batter, ipl_data,seasons, venues)  
    equal_angle = 45  
    source = pd.DataFrame({
        "Zones": zones, 
        "value": [equal_angle] * len(zones), 
        "shots": values,
        "angle": [i * equal_angle + equal_angle / 2 for i in range(len(zones))] 
    })

    chart = alt.Chart(source).mark_arc(innerRadius=50).encode(
        theta=alt.Theta(field="value", type="quantitative"),  
        color=alt.Color(field="Zones", type="nominal"),
        tooltip=["Zones", "shots"]  
    )
    

    text = alt.Chart(source).mark_text(size=12, color='black').encode(
        theta=alt.Theta(field="angle", type="quantitative"), 
        radius=alt.value(100), 
        text=alt.Text(field="shots", type="quantitative")  
    )
    

    final_chart = chart + text
    

    st.altair_chart(final_chart.properties(
        title="Cricket Wagon Wheel: Shot Distribution by Region"
    ))