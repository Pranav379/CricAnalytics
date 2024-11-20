import pandas as pd

df = pd.read_csv("../data/ipl-hawkeye-data.csv")

def attacking_shots(df, playername, ground, year):

    #New data frame to filter based on batter, year, and ground
    df2 = df.copy()
    if ((ground is None) and (year is None)):
        df2 = df[df['bat'] == playername]
    else:
        df2 = df[(df['bat'] == playername) & (df['season'] == year) & (df['ground'] == ground)]
    

    shot_types = df2.groupby('shot')
    shot_output = shot_types.agg(
        runs_scored = ('batruns', 'sum'),
        dismissal_count = ('out', 'sum'),
        balls = ('batruns', 'count'),
        control = ('control', 'mean')
    )


    #New column for rpb
    shot_output['RPB'] = shot_output['runs_scored'] / shot_output['balls']
    
    #Average rpb for all shots
    average = shot_output['runs_scored'].sum() / shot_output['balls'].sum()

    #Classify as attacking shot
    shot_output['Attacking'] = shot_output['RPB'].apply(lambda x: 1 if x > average else 0)
    
    #Attack pct
    attacking = shot_output.loc[shot_output['Attacking'] == 1]
    total_attack_balls = attacking['balls'].sum()
    attack_pct = 100 * total_attack_balls / shot_output['balls'].sum()


    #Attacking efficacy 
    total_attack_runs = attacking['runs_scored'].sum()
    attack_efficacy = total_attack_runs / total_attack_balls

    #How much control
    control_pct = (shot_output['control'].mean()) * 100

    #Returns attacking stats
    attacking = {
        "Attacking Shot %" : attack_pct,
        "Attacking Efficacy" : attack_efficacy,
        "Batter Control %" : control_pct
    }

    return attacking

