import numpy as np
import pandas as pd

def average_deviation(df):
    df['over_number'] = np.floor(df['ball_id']) + 1
    player_list = df['bowl'].unique()
    deviation_list = []
    for player in player_list:
        player_data = df[df['bowl'].str.contains(player)]
        
        power_over_df = player_data[(player_data['over_number'] <= 6)]
        power_ball_df = power_over_df[(player_data['wide'] == 0) & (player_data['noball'] == 0) ]
        
        power_ball_count = power_ball_df.count(axis='columns').shape[0]
        
        if power_ball_count == 0:  
            continue
            
        deviation = np.abs(power_ball_df['deviation']).sum()/power_ball_count
        
        deviation_list.append(deviation)
        
    overall_avg_deviation = np.sum(deviation_list)/len(deviation_list)
    return overall_avg_deviation

def average_control(df):
    avg_control = df['control'].sum()/df.count(axis='columns').shape[0]
    return avg_control

def bowling_agg_stats(df, player_name, year, venue):
    # filter the data to include only records for the specified player
    player_data = df[df['bowl'].str.contains(player_name)]
    player_data['runs_conceded'] = player_data['batruns'] + player_data['noball'] + player_data['wide']
    player_data['over_number'] = np.floor(player_data['ball_id']) + 1
    unique_games = player_data.drop_duplicates(subset=['p_match'])
    
    # get the games
    game = len(unique_games)
    
    # get the overs bowled
    ball_df = player_data[(player_data['wide'] == 0) & (player_data['noball'] == 0) ]
    ball_count = ball_df.count(axis='columns').shape[0]
    over_int = ball_count // 6
    over_decimal = ball_count % 6
    over_val = over_int + over_decimal/10

    # get the runs conceded
    runs = player_data['runs_conceded'].sum()
    
    # economy
    economy = runs/over_val
    
    # power ower percentage
    power_over_df = player_data[(player_data['over_number'] <= 6)]
    power_ball_df = power_over_df[(player_data['wide'] == 0) & (player_data['noball'] == 0) ]
    power_ball_count = power_ball_df.count(axis='columns').shape[0]
    
    power_percentage = power_ball_count/ball_count
    
    power_avg_control = average_control(power_ball_df)

    # deviation stats
    player_deviation = np.abs(power_ball_df['deviation']).sum()/power_ball_count
    avg_deviation = average_deviation(df)
    isGreaterThanAvg = player_deviation > avg_deviation
    
    # middle over pecentage
    middle_over_df = player_data[((player_data['over_number'] > 6) & (player_data['over_number'] < 16))]
    middle_ball_df = middle_over_df[(middle_over_df['wide'] == 0) & (middle_over_df['noball'] == 0) ]
    middle_ball_count = middle_ball_df.count(axis='columns').shape[0]
    
    middle_percentage = middle_ball_count/ball_count
    
    middle_avg_control = average_control(middle_ball_df)
    
    # death over percentage
    death_over_df = player_data[(player_data['over_number'] >= 16)]
    death_ball_df = death_over_df[(death_over_df['wide'] == 0) & (death_over_df['noball'] == 0) ]
    death_ball_count = death_ball_df.count(axis='columns').shape[0]
    
    death_percentage = death_ball_count/ball_count

    death_avg_control = average_control(death_ball_df)

    stats = {
        "Games": game,
        "Overs" : over_val,
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