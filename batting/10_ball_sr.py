
import pandas as pd


def calculate_10_ball_sr(df, batter_name):
    batter_data = df[df['bat'] == batter_name]
    if 'batruns' not in batter_data.columns:
        return "Column 'batruns' not found in data."
        
    #filters for only the first 10 balls
    first_10 = batter_data.head(10)
    
    #sums up score for those first 10 balls
    total_runs = first_10['batruns'].sum()

    if len(first_10) < 10:
        return None
    else:
        strike = (total_runs/10)*100
        
        #gets the strikerate
        SR = {
        "10 Ball Sr": strike
    }
        
        return SR
    
