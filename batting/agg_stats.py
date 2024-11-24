
def player_agg_stats(df, player_name, seasons = None, venues = None):

    #filter the data to include only records for the specified player
    player_data = df[df['bat'] == player_name]

    if seasons:
        player_data = player_data.loc[df['season'].isin(seasons)]

    if venues:
        player_data = player_data.loc[df['ground'].isin(venues)]
    
    #calculate total runs scored
    total_runs = player_data['batruns'].sum()
    
    #count total dismissals
    total_dismissals = player_data['out'].sum()  #'out' is 1 if dismissed, 0 otherwise
    
    # Calculate Dot % (percentage of dot balls faced)
    # do not include balls with wides for balls faced
    valid_balls = player_data[(player_data['wide'] == 0)]

    total_balls_faced = valid_balls.shape[0]
    
    #count dot balls only from valid balls (excluding extras)
    dot_balls = valid_balls[valid_balls['batruns'] == 0].shape[0]
    dot_percentage = (dot_balls / total_balls_faced) * 100 if total_balls_faced > 0 else 0
    
    #calculate Boundary % (percentage of boundaries, 4s or 6s)
    boundaries = valid_balls[valid_balls['batruns'].isin([4, 6])].shape[0]
    boundary_percentage = (boundaries / total_balls_faced) * 100 if total_balls_faced > 0 else 0
    
    #store results in a dictionary
    stats = {
        "Runs": total_runs,
        "Balls" : total_balls_faced,
        "Dismissals": total_dismissals,
        "Dot %": dot_percentage,
        "Boundary %": boundary_percentage
    }
    
    return stats

