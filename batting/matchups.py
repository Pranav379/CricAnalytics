# Calculates the strike rate 
def get_matchup_stats(df, player_name, bowling_type, pace_min= None, pace_max= None, deviation_min=None, deviation_max=None):    
    #accounts for pace calculations
    if pace_max is not None:
        df = df.loc[(df['release_speed'] < pace_max)]
    if pace_min is not None:
        df = df.loc[(df['release_speed'] > pace_min)]
        
    #accounts for deviation
    if deviation_max is not None:
        df = df.loc[(df['deviation'] < deviation_max)]
    if deviation_min is not None:
        df = df.loc[(df['deviation'] > deviation_min)]
    
    #fetches specific player
    player_data = df[(df['bat'] == player_name) & (df['bowl_style'] == bowling_type)]
    
    # Exclude byes and legbyes as they are insufficent 
    player_data = player_data[
        (player_data['wide'] == 0) 
    ]

    
    #calculates strike rate by getting bowl_style
    total_balls = player_data.shape[0]
    #Exclude noballs and wides for runs
    player_data = player_data[
        (player_data['byes'] == 0) &
        (player_data['legbyes'] == 0)
    ]
    
    total_runs = player_data['batruns'].sum()
    total_dismissals = int(player_data['dismissal'].dropna().count())
    
    #Avoids divison by zero
    if total_balls == 0:
        strike_rate = None
    else:
        strike_rate = round((total_runs / total_balls) * 100)
        
    #formats stats and return
    stats = {
        "Total Balls": total_balls,
        "Strike Rate": strike_rate,
        "Dismissals": total_dismissals
    }
    
    return stats