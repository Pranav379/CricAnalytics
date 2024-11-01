import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('data/ipl-hawkeye-data.csv')

# Calculates the strike rate 
def get_matchup_stats(player_name, bowling_type, pace_min= None, pace_max= None, deviation_min=None, deviation_max=None):
    #fetches specific player
    player_data = df[(df['bat'] == player_name) & (df['bowl_style'] == bowling_type)]
    #accounts for pace calculations
    if pace_max != None:
        player_data = df.loc[(df['release_speed'] < pace_max)]
    if pace_min != None:
        player_data = df.loc[(df['release_speed'] > pace_min)]
    #accounts for deviation
    if deviation_max != None:
        player_data = df.loc[(df['deviation'] < deviation_max)]
    if pace_min != None:
        player_data = df.loc[(df['deviation'] > pace_min)]
    #calculates strike rate by getting bowl_style
    player_vs_bowl = player_data.groupby('bowl_style')['batruns']
    total_balls = player_vs_bowl.shape[0]
    strike_r_by_player = player_vs_bowl.mean().mul(100)    
    #formats stats and return
    stats = {
        "Total Balls": total_balls,
        "Strike Rate": strike_r_by_player
    }
    return stats


#Create a bar chart
s = get_matchup_stats('Virat Kohli', 'RM')
print(s)