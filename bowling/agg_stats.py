import numpy as np
import pandas as pd

def average_deviation(df):
    df['over_number'] = np.floor(df['ball_id']) + 1
    player_list = df['bowl'].unique()
    deviation_list = []
    for player in player_list:
        player_data = df[df['bowl'].str.contains(player)]
        
        power_over_df = player_data[(player_data['over_number'] <= 6)]
        power_ball_df = power_over_df[(power_over_df['wide'] == 0) & (power_over_df['noball'] == 0)]
        
        power_ball_count = power_ball_df.shape[0]
        
        if power_ball_count == 0:  
            continue
            
        deviation = np.abs(power_ball_df['deviation']).sum() / power_ball_count
        deviation_list.append(deviation)
        
    if len(deviation_list) == 0: 
        return 0
    
    overall_avg_deviation = np.sum(deviation_list) / len(deviation_list)
    return overall_avg_deviation

def average_control(df):
    total_rows = df.shape[0]
    if total_rows == 0:  
        return 0
    return df['control'].sum() / total_rows

def bowling_agg_stats(df, player_name, seasons=None, venues=None):

    player_data = df 
    
    player_data = player_data[player_data['bowl'].str.contains(player_name)]

    if seasons:
        player_data = player_data.loc[player_data['season'].isin(seasons)]

    if venues:
        player_data = player_data.loc[player_data['ground'].isin(venues)]

    player_data['runs_conceded'] = player_data['batruns'] + player_data['noball'] + player_data['wide']
    player_data['over_number'] = np.floor(player_data['ball_id']) + 1
    unique_games = player_data.drop_duplicates(subset=['p_match'])

    # Number of games
    games = len(unique_games)
    
    # Overs bowled
    ball_df = player_data[(player_data['wide'] == 0) & (player_data['noball'] == 0)]
    ball_count = ball_df.shape[0]
    over_val = ball_count // 6 + (ball_count % 6) / 10 if ball_count > 0 else 0

    # Runs conceded
    runs = player_data['runs_conceded'].sum()
    
    # Economy
    economy = runs / over_val if over_val > 0 else 0

    # Power over stats
    power_over_df = player_data[(player_data['over_number'] <= 6)]
    power_ball_df = power_over_df[(power_over_df['wide'] == 0) & (power_over_df['noball'] == 0)]
    power_ball_count = power_ball_df.shape[0]
    
    power_percentage = power_ball_count / ball_count if ball_count > 0 else 0
    power_avg_control = average_control(power_ball_df)

    # Deviation stats
    player_deviation = (
        np.abs(power_ball_df['deviation']).sum() / power_ball_count if power_ball_count > 0 else 0
    )
    avg_deviation = average_deviation(df)
    isGreaterThanAvg = player_deviation > avg_deviation

    # Middle over stats
    middle_over_df = player_data[(player_data['over_number'] > 6) & (player_data['over_number'] < 16)]
    middle_ball_df = middle_over_df[(middle_over_df['wide'] == 0) & (middle_over_df['noball'] == 0)]
    middle_ball_count = middle_ball_df.shape[0]
    
    middle_percentage = middle_ball_count / ball_count if ball_count > 0 else 0
    middle_avg_control = average_control(middle_ball_df)

    # Death over stats
    death_over_df = player_data[(player_data['over_number'] >= 16)]
    death_ball_df = death_over_df[(death_over_df['wide'] == 0) & (death_over_df['noball'] == 0)]
    death_ball_count = death_ball_df.shape[0]
    
    death_percentage = death_ball_count / ball_count if ball_count > 0 else 0
    death_avg_control = average_control(death_ball_df)

    stats = {
        "Games": games,
        "Overs": over_val,
        "Economy": economy,
        "Power_Percentage": power_percentage,
        "Power_Control": power_avg_control, 
        "Player_Deviation": player_deviation,
        "Average_Deviation": avg_deviation,
        "Deviation_Comparison": isGreaterThanAvg,
        "Middle_Percentage": middle_percentage,
        "Middle_Control": middle_avg_control,
        "Death_Percentage": death_percentage,
        "Death_Control": death_avg_control
    }
    
    return stats
