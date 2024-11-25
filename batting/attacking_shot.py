import pandas as pd


def attacking_shots(df, playername = None, ground = None, year = None):

    #New data frame to filter based on batter, year, and ground
    df2 = df.copy()

    if playername:
        df2 = df.loc[df['bat'] == playername]
    
    if ground:
        df2 = df2.loc[(df2['ground'].isin(ground))]
    
    if year:
        df2 = df2.loc[(df2['season'].isin(year))]

    
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
        "Batter Control %" : control_pct,
        "Shot Data": shot_output
    }

    return attacking

