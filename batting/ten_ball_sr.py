

def calculate_10_ball_sr(df, batter_name, seasons = None, venues = None):

    batter_data = df.loc[(df['bat'] == batter_name)]

    if seasons:
        batter_data = batter_data.loc[batter_data['season'].isin(seasons)]

    if venues:
        batter_data = batter_data.loc[batter_data['ground'].isin(venues)]

    if 'batruns' not in batter_data.columns:
        return "Column 'batruns' not found in data."
        
    #excludes wides
    legit_balls = batter_data[batter_data['wide'] == 0]
        
    groups = legit_balls.groupby(['p_match', 'inns'])
    game_srs = []

    #iterate through each match inning for batter
    for _, group in groups:
        first_10 = group.head(10)

        total_runs = first_10['batruns'].sum()
        
        # skip if less than 10 balls
        if len(first_10) < 10:
            continue
            
        game_sr = (total_runs / 10) * 100
        game_srs.append(game_sr)

    if game_srs:
        avg_sr = sum(game_srs) / len(game_srs)
        games_count = len(game_srs)
    else:
        avg_sr, games_count = None, 0

    return {
        "Average 10 Ball SR": avg_sr,
        "Games Considered" : games_count
    }

                
    
