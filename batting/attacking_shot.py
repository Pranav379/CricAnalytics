import pandas as pd

df = pd.read_csv("./data/ipl-hawkeye-data.csv")

#Function to identify attacking shots
def attacking_shots(df, playername, season):
    shot_types = df.groupby('shot')
    shot_output = shot_types.agg(
        runs_scored = ('batruns', 'sum'),
        dismissal_count = ('out', 'sum'),
        balls = ('batruns', 'count')
    )

    total_runs = shot_output['runs_scored'].sum()
    total_balls = shot_output['balls'].sum()

    #Average rpb
    average = total_runs / total_balls

    #New column for rpb
    shot_output['rpb'] = shot_output['runs_scored'] / shot_output['balls']
    shot_output['type_of_shot'] = "Non-Attacking"

    #Classify as attacking shot
    attack_shot = 0
    if(shot_output['rpb'] > average):
        shot_output['type_of_shot'] = "Attacking"
        attack_shot += 1
    
    #Attacking shot %
    attack_pct = (attack_shot / total_balls) * 100

    #Attacking efficacy
    attack_efficacy = (attack_pct / 100) * average

    #How much control
    control_pct = (df['control'].sum() / total_balls) * 100

    #Returns attacking stats
    attacking = {
        "Attacking Shot %" : attack_pct,
        "Attacking Efficacy" : attack_efficacy,
        "Batter Control %" : control_pct
    }

    return attacking


print(attacking_shots(df, "Virat Kohli", 2024))


    


