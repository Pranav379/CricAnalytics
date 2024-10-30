import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('data/ipl-hawkeye-data.csv')
# def get_matchup(player):
#    player_data = df[df['bat'] == player] #Filters for specific player
#    avg_scores = player_data.groupby('bowl_type')['score'].mean().reset_index()
#    avg_scores = avg_scores.rename(columns={'score': 'average_runs'})
#    return avg_scores


# Calculates the strike rate 
def get_matchup_stats(player_name, bowling_type, pace_min= None, pace_max= None):
    player_data = df[df['bat'] == player_name]
    if pace_max != None:
        player_data = df.loc[(df['release_speed'] < pace_max)]
    if pace_min != None:
        player_data = df.loc[(df['release_speed'] > pace_min)]
    strike_r_by_player = player_data.groupby('bowl_style')['batruns'].mean().mul(100).reset_index()        
    return strike_r_by_player



